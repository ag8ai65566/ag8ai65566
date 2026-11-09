"""Voice Studio: a personal platform for consent-gated voice datasets, cloud fine-tuning and local TTS."""
__version__ = "0.1.0"

try:  # verify HTTPS against the OS certificate store, so antivirus HTTPS scanning (Norton, Kaspersky …) and company
    import truststore  # proxies do not break RunPod, S3 and Hugging Face; done before httpx / boto3 are imported
    truststore.inject_into_ssl()
except ImportError:
    pass
