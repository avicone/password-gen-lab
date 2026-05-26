def print_message(message, level="info"):
    valid_levels = ["info", "success", "error"]
    if level not in valid_levels:
        raise ValueError(f"Unknown level '{level}'. Use: {', '.join(valid_levels)}")
    prefix = {"info": "[*]", "success": "[OK]", "error": "[ERROR]"}.get(level, "[*]")
    print(f"{prefix} {message}")