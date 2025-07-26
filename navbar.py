import textwrap

def render_navbar():
    return textwrap.dedent("""
    <header class="header">
        <nav class="navbar">
            <div class="logo">
                <img src="https://i.postimg.cc/jSj1dZHG/Screenshot-2025-07-24-193200-removebg-preview.png" alt="Logo" class="logo-img">
            </div>
            <input type="checkbox" id="menu-toggle" style="display: none;">
            <label class="hamburger" for="menu-toggle">
                <span></span>
                <span></span>
                <span></span>
            </label>
            <ul class="navbar-list">
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="Home">
                        <input class="nav-button" type="submit" value="🏠 Home">
                    </form>
                </li>
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="Dashboard">
                        <input class="nav-button" type="submit" value="📊 Dashboard">
                    </form>
                </li>
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="About">
                        <input class="nav-button" type="submit" value="ℹ️ About">
                    </form>
                </li>
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="Contact">
                        <input class="nav-button" type="submit" value="📞 Contact">
                    </form>
                </li>
            </ul>
        </nav>
    </header>
    """)
