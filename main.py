# -*- coding: utf-8 -*-
# Tool : User-Agent Generator v3.0 PRO+
# Dev  : GPT-5 Custom Version (for Termux)
# Date : 2025

import random, time, os
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text

console = Console()

# Color print helper
def cprint(text, style="green"):
    console.print(text, style=style)

# ─────────────────────────────────────────────
# Banner
def banner():
    os.system("clear")
    banner_art = """[bold cyan]
░█▀█░█░█░█▀█░█▀▀░█░█
░█▀█░█▀▄░█▀█░▀▀█░█▀█
░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀
[/bold cyan]"""
    title = Text("🔥 USER-AGENT GENERATOR v3.0 PRO+ 🔥", style="bold magenta")
    desc = Text("Generate ultra-realistic active UAs (2005 → 2025)", style="bold green")
    box = Panel.fit(f"{banner_art}\n{title}\n{desc}", border_style="bold blue", padding=(1, 4))
    console.print(box)

# ─────────────────────────────────────────────
# Data pools
android_versions = [str(v) for v in range(4, 15)]
ios_versions = [f"{i}.{j}" for i in range(9, 18) for j in range(0, 6)]
windows_versions = ["7", "8", "8.1", "10", "11"]
years = list(range(2005, 2025))

models = [
    # Android
    "Samsung Galaxy S23", "Samsung Galaxy A14", "Samsung Galaxy S10", "Redmi Note 12", "Redmi Note 11",
    "Infinix Hot 12", "Vivo Y20", "Realme 9 Pro", "Oppo F19 Pro", "Tecno Camon 20", "Huawei P30", "Pixel 8 Pro",
    "Lenovo K10", "Nokia 8.1", "HTC One M8", "LG G6",
    # Old phones
    "Nokia N73", "Nokia 6600", "Sony Ericsson K750i", "Motorola RAZR V3", "BlackBerry Bold 9700",
    "Windows Phone Lumia 920", "iPhone 5S", "iPhone 6", "iPhone 13 Pro", "iPhone 15 Pro Max"
]

builds = [
    "QP1A.190711.020", "SP1A.210812.016", "TP1A.220624.014",
    "UP1A.230905.007", "RP1A.200720.012", "LMY48B", "IMM76D", "JOP40C"
]

browsers = [
    "Mozilla/5.0", "Dalvik/2.1.0", "Opera/9.80", "Chrome", "FB4A", "Instagram", "UCBrowser", "Edge"
]

# ─────────────────────────────────────────────
def generate_user_agent():
    base = random.choice(browsers)
    year = random.choice(years)

    if "Mozilla" in base:
        android_version = random.choice(android_versions)
        model = random.choice(models)
        return f"Mozilla/5.0 (Linux; Android {android_version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,160)}.0.{random.randint(1000,9999)}.80 Mobile Safari/537.36"

    elif "Dalvik" in base:
        model = random.choice(models)
        android_version = random.choice(android_versions)
        build = random.choice(builds)
        return f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build})"

    elif "Opera" in base:
        return f"Opera/9.80 (Android; Opera Mini/{random.randint(20,99)}.{random.randint(0,9)}.{random.randint(100,999)}/{random.randint(30,90)}.{random.randint(0,9)}; U; en) Presto/2.12.{random.randint(100,999)} Version/{random.randint(10,15)}.00"

    elif "FB4A" in base:
        android_version = random.choice(android_versions)
        model = random.choice(models)
        return f"Mozilla/5.0 (Linux; Android {android_version}; {model}) [FBAN/FB4A;FBAV/{random.randint(300,400)}.0.0.{random.randint(10,99)}.{random.randint(100,999)};FBCR/Android;FBBV/{random.randint(100000,999999)}]"

    elif "Instagram" in base:
        android_version = random.choice(android_versions)
        model = random.choice(models)
        build = random.choice(builds)
        return f"Instagram {random.randint(300,400)}.0.0.{random.randint(10,99)}.{random.randint(100,999)} Android ({android_version}/{model}; Build/{build}; en_US)"

    elif "UCBrowser" in base:
        return f"Mozilla/5.0 (Linux; U; Android {random.choice(android_versions)}; en-US; {random.choice(models)}) AppleWebKit/534.31 (KHTML, like Gecko) UCBrowser/{random.randint(10,15)}.{random.randint(0,9)}.{random.randint(100,999)} Mobile Safari/534.31"

    elif "Edge" in base:
        win_ver = random.choice(windows_versions)
        return f"Mozilla/5.0 (Windows NT {win_ver}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,140)}.0.{random.randint(1000,9999)}.0 Safari/537.36 Edg/{random.randint(100,140)}.0.{random.randint(1000,9999)}.0"

    else:
        return f"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT {random.choice(windows_versions)}; Trident/6.0)"

# ─────────────────────────────────────────────
def cli_main():
    banner()
    count = int(console.input("\n[bold yellow]📦 How many UAs you want to generate? [/bold yellow]"))
    filename = "/sdcard/Download/generated_UA_PRO3.txt"

    with open(filename, "w") as f:
        for _ in track(range(count), description="[cyan]⚙️ Generating Smart Active User-Agents...[/cyan]"):
            f.write(generate_user_agent() + "\n")
            time.sleep(0.02)

    console.print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="dim")
    cprint(f"✅ Successfully generated {count} realistic user-agents (2005–2025).", "bold green")
    cprint(f"📁 Saved to: {filename}", "bold cyan")
    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="dim")

    cprint("\n✨ Done! Use them in your tools or Facebook Graph requests.", "bold yellow")

# ─────────────────────────────────────────────
if __name__ == "__main__":
    cli_main()
