import logging
import colorlog

# 🎯 Fungsi untuk buat logger modular per modul
def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    logger = colorlog.getLogger(name)

    if not logger.handlers:
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        ))
        logger.addHandler(handler)
        logger.setLevel(level)
        logger.propagate = False  # Hindari duplikasi log

    return logger

