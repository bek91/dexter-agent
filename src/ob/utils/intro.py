def print_intro():
    """Display the welcome screen with ASCII art."""
    # ANSI color codes
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # Clear screen effect with some spacing
    print("\n" * 2)
    
    # Welcome box with light blue border
    box_width = 70
    welcome_text = "Welcome to the Jungle"
    padding = (box_width - len(welcome_text) - 2) // 2
    
    print(f"{LIGHT_BLUE}{'═' * box_width}{RESET}")
    print(f"{LIGHT_BLUE}║{' ' * padding}{BOLD}{welcome_text}{RESET}{LIGHT_BLUE}{' ' * (box_width - len(welcome_text) - padding - 2)}║{RESET}")
    print(f"{LIGHT_BLUE}{'═' * box_width}{RESET}")
    print()
    
    # ASCII art for ob in block letters (financial terminal style)
    ob_art = f"""{BOLD}{LIGHT_BLUE}
    █████╗  ██████╗ ███████╗███╗   ██╗████████╗     ██████╗ ██████╗ 
   ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝    ██╔═══██╗██╔══██╗
   ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║       ██║   ██║██████╔╝
   ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║       ██║   ██║██╔══██╗
   ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║       ╚██████╔╝██████╔╝
   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝ ╚═════╝
{RESET}"""
    
    print(ob_art)
    print()
    print("Your AI employee")
    print("Ask me any questions. Type 'exit' or 'quit' to end.")
    print()

