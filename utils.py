def print_message(message, level="info"):
    prefix = {"info": "[*]", "success": "[OK]", "error": "[ERROR]"}.get(level, "[*]")
    print(f"{prefix} {message}")
