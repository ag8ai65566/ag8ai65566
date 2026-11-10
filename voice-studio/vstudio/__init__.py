"""Voice Studio: a personal platform for consent-gated voice datasets, cloud fine-tuning and local TTS."""
__version__ = "0.1.0"


def _trust_windows_certificates() -> None:
    """Verify HTTPS (RunPod, its S3 storage, Hugging Face, and the uv/pip runs the studio starts) against the roots
    Windows trusts as well as certifi's, so antivirus HTTPS scanning (Norton, Kaspersky …) and company proxies whose
    root is installed in Windows do not break it.

    One CA file, set through the variables httpx, requests, botocore and uv read, and verified by OpenSSL itself.
    (Patching ssl.SSLContext with truststore was not thread-safe: while one connection was handshaking, others
    sharing the context, as boto3's parallel transfers do, could be checked with verification switched off.)
    Variables a person set themselves are kept."""
    import os
    import ssl
    import tempfile
    from pathlib import Path

    if not hasattr(ssl, "enum_certificates"):  # Windows only; elsewhere certifi's roots are used as before
        return
    path = Path(tempfile.gettempdir()) / "voice-studio-ca.pem"
    if os.environ.get("SSL_CERT_FILE") != str(path):  # once per process
        pems, seen = [], set()
        try:
            import certifi
            pems.append(Path(certifi.where()).read_text(encoding="utf-8"))
        except (ImportError, OSError):
            pass
        for store in ("CA", "ROOT"):  # the stores ssl.create_default_context() reads on Windows
            for der, encoding, trust in ssl.enum_certificates(store):
                if encoding == "x509_asn" and (trust is True or "1.3.6.1.5.5.7.3.1" in trust) and der not in seen:
                    seen.add(der)  # trusted for server authentication
                    pems.append(ssl.DER_cert_to_PEM_cert(der))
        tmp = path.with_name(f"{path.name}.{os.getpid()}.tmp")
        tmp.write_text("\n".join(pems), encoding="utf-8")
        os.replace(tmp, path)
    for var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "AWS_CA_BUNDLE"):
        os.environ.setdefault(var, str(path))


try:
    _trust_windows_certificates()
except Exception:  # never block start-up: without it, HTTPS falls back to certifi's roots
    pass
