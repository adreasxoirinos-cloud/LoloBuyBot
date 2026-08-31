import os
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from aiohttp import web

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = discord.Object(id=1543959901393391678)

class LoloBuyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"Logged in safely as {self.user.name}... Ready!")
        print("Use !sync in your server to activate application slash commands.")

bot = LoloBuyBot()

async def handle(request):
    return web.Response(text="LoloBuy Bot Alive Matrix Active")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server routing successfully bound to port {port}")

@bot.command(name="sync")
@commands.is_owner()
async def sync(ctx):
    await ctx.send("Starting application command framework synchronization matrix...")
    try:
        bot.tree.copy_to(guild=GUILD_ID)
        synced = await bot.tree.sync(guild=GUILD_ID)
        await ctx.send(f"Successfully registered {len(synced)} slash commands to this server!")
    except Exception as e:
        await ctx.send(f"Sync failed: {e}")

@bot.tree.command(name="prohibited", description="Check DHL Compliance Logistics rules.")
@app_commands.describe(category="Select the cargo type to inspect compliance parameters")
@app_commands.choices(category=[
    app_commands.Choice(name="Apparel", value="apparel"),
    app_commands.Choice(name="Bags & Luggage", value="bags"),
    app_commands.Choice(name="Electronics & Watches", value="electronics"),
    app_commands.Choice(name="Cosmetics", value="cosmetics"),
    app_commands.Choice(name="Food & Medicine", value="food"),
    app_commands.Choice(name="Toys", value="toys"),
    app_commands.Choice(name="Books & Adult Products", value="books")
])
async def prohibited(interaction: discord.Interaction, category: app_commands.Choice[str]):
    embed = discord.Embed(title=f"📋 DHL Logistics Compliance Matrix: {category.name}", color=0xFFCC00)
    if category.value == "apparel":
        embed.add_field(name="🟢 Transportable", value="Standard fabrics, unbranded clothing, cotton items.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Luxury replicas, branded designer gear.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Wet garments, hazardous industrial textiles.", inline=False)
    elif category.value == "bags":
        embed.add_field(name="🟢 Transportable", value="Canvas backpacks, unbranded nylon luggage.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Counterfeit luxury leather purses, brand metal clasps.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Bags containing prohibited items or hidden lithium power banks.", inline=False)
    elif category.value == "electronics":
        embed.add_field(name="🟢 Transportable", value="Cables, non-battery hardware panels.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Built-in lithium battery devices, smartwatches.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Loose standalone power banks, loose cells, uncertified liquids.", inline=False)
    elif category.value == "cosmetics":
        embed.add_field(name="🟢 Transportable", value="Solid makeup accessories, dry makeup sponges.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Creams, setting sprays, lip gloss powders.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Flammable aerosol sprays, high-volume industrial chemical containers.", inline=False)
    elif category.value == "food":
        embed.add_field(name="🟢 Transportable", value="Completely sealed dry goods, snack wafers.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Spices, vacuum-sealed local regional tea items.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Raw meats, fresh vegetables, unverified prescription medicines.", inline=False)
    elif category.value == "toys":
        embed.add_field(name="🟢 Transportable", value="Standard plastic building blocks, plushies.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Electronic rc elements, magnets, wired dolls.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Replica weapons, explosive caps, toxic gel beads.", inline=False)
    elif category.value == "books":
        embed.add_field(name="🟢 Transportable", value="Standard illustrative prints, non-political paperbacks.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="High-volume heavy weight catalog binding sets.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Illegal adult videos, dangerous political prints.", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="coupons", description="View registration rewards and affiliate accelerator.")
async def coupons(interaction: discord.Interaction):
    embed = discord.Embed(title="🎁 LoloBuy Welcome Package & Rewards", color=0x2ECC71)
    embed.description = (
        "Join today and claim your platform registration gifts:\n\n"
        "• **15% OFF** Shipping Coupon\n"
        "• **10% OFF** Secondary Weight Coupon\n"
        "• **$500 Coupon Bundle** for new warehouse users!\n\n"
        "👉 [Click here to register your account and activate rewards!](https://lolobuy.com)"
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="convert", description="Convert Chinese Yuan (CNY) to international baseline metrics.")
@app_commands.describe(cny="The cost value in Chinese Yuan (e.g. 500)")
async def convert(interaction: discord.Interaction, cny: float):
    usd = cny * 0.14
    eur = cny * 0.13
    gbp = cny * 0.11
    embed = discord.Embed(title="💱 CNY Live Conversion Card", color=0x3498DB)
    embed.add_field(name="🇨🇳 Chinese Yuan", value=f"**{cny:.2f} CNY**", inline=False)
    embed.add_field(name="🇺🇸 US Dollar", value=f"${usd:.2f} USD", inline=True)
    embed.add_field(name="🇪🇺 Euro", value=f"€{eur:.2f} EUR", inline=True)
    embed.add_field(name="🇬🇧 British Pound", value=f"£{gbp:.2f} GBP", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="yupoo", description="Guide on searching catalogs via Yupoo platform engines.")
async def yupoo(interaction: discord.Interaction):
    embed = discord.Embed(title="📸 Yupoo Catalog Navigation Guide", color=0x9B59B6)
    embed.description = (
        "1. Browse through your preferred seller's Yupoo image gallery.\n"
        "2. Copy the item specific product data keys or direct photo title details.\n\n"
        "⚠️ **CRITICAL WARNING:** Do **NOT** paste raw `yupoo.com` URLs into the main LoloBuy search fields. The engine cannot index them. Instead, extract and submit the valid **Weidian, Taobao, or 1688 link** listed on the seller's page."
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="track", description="Learn how to monitor international waybills.")
async def track(interaction: discord.Interaction):
    embed = discord.Embed(title="📦 3-Step Parcel Tracking Portal Sequence", color=0x5DADE2)
    embed.add_field(name="Step 1: Get Code", value="Go to your LoloBuy Profile Order panel and extract your international shipment waybill string.", inline=False)
    embed.add_field(name="Step 2: External Validation", value="Copy that unique alphanumeric sequence code.", inline=False)
    embed.add_field(name="Step 3: Global Tracking", value="Paste the sequence code directly into automated global parcel data sites like [17track](https://17track.net) for live milestones.", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="estimator", description="Shipping Freight Cost Calculation Tutorial.")
async def estimator(interaction: discord.Interaction):
    embed = discord.Embed(title="⚖️ Shipping Freight & Volume Cost Estimation", color=0xE67E22)
    embed.description = (
        "Before placing your orders, utilize the platform's cost tool:\n\n"
        "• Weigh parameters are processed based on volumetric mass or true scale values.\n"
        "• Select your destination country network to filter matching shipping networks.\n"
        "• Review approximate price speed tier differences between lines before checkout."
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="rehearsal", description="Learn how Warehouse Rehearsal Packaging saves money.")
async def rehearsal(interaction: discord.Interaction):
    embed = discord.Embed(title="📦 Rehearsal Packaging Warehouse Optimization", color=0x1ABC9C)
    embed.description = (
        "Want to know your true shipping cost upfront? Use rehearsal packing:\n\n"
        "• Warehouse logistics staff pre-pack your selected cart items into a real box.\n"
        "• This calculates the **exact physical dimensions and weight metrics** before you pay.\n"
        "• Bypasses estimated freight overcharges, preventing surprise budget corrections later!"
    )
    await interaction.response.send_message(embed=embed)

# Command 8: /lines
@bot.tree.command(name="lines", description="Get recommended shipping lines for your destination region.")
@app_commands.describe(region="Select your shipping destination region")
@app_commands.choices(region=[
    app_commands.Choice(name="Europe (EU)", value="eu"),
    app_commands.Choice(name="United States & Canada (NA)", value="na"),
    app_commands.Choice(name="United Kingdom (UK)", value="uk")
])
async def lines(interaction: discord.Interaction, region: app_commands.Choice[str]):
    embed = discord.Embed(title=f"✈️ Recommended Shipping Routes: {region.name}", color=0x9B59B6)
    if region.value == "eu":
        embed.add_field(name="🥇 Top Choice: LoloBuy Tax-Free (Tariffless)", value="Speed: 10-14 Days\nSafety: 10/10 (Bypasses custom taxes safely). Best for branded items.", inline=False)
        embed.add_field(name="🥈 Economy Choice: DHL Packet", value="Speed: 14-22 Days\nSafety: 8/10. Best for low-weight, unbranded hauls.", inline=False)
    elif region.value == "na":
        embed.add_field(name="🥇 Top Choice: KR-EMS (Actual Weight)", value="Speed: 7-12 Days\nSafety: 9/10. Fast delivery, billed by real mass weight.", inline=False)
        embed.add_field(name="🥈 Economy Choice: US-Line Small", value="Speed: 12-18 Days\nSafety: 8/10. Perfect for small packages under 2kg.", inline=False)
    elif region.value == "uk":
        embed.add_field(name="🥇 Top Choice: UK Line-T", value="Speed: 8-12 Days\nSafety: 10/10. Highly stable tracking metrics, royal mail delivery.", inline=False)
    embed.set_footer(text="Tip: Always buy shipping insurance for your peace of mind!")
    await interaction.response.send_message(embed=embed)

# Command 9: /volumetric
@bot.tree.command(name="volumetric", description="Calculate the volumetric package weight used by logistics lines.")
@app_commands.describe(length="Length of the box in cm", width="Width of the box in cm", height="Height of the box in cm")
async def volumetric(interaction: discord.Interaction, length: float, width: float, height: float):
    vol_weight = (length * width * height) / 5000
    embed = discord.Embed(title="📐 Volumetric Weight Estimation Matrix", color=0xE67E22)
    embed.description = (
        f"Box Dimensions: {length} x {width} x {height} cm\n\n"
        f"📊 Estimated Volumetric Weight: {vol_weight:.2f} kg\n\n"
        "⚠️ Logistics Note: Shipping lines will charge you based on whichever number is higher—the true physical scale weight or this volumetric weight calculation!"
    )
    await interaction.response.send_message(embed=embed)

# Command 10: /status
@bot.tree.command(name="status", description="Decode confusing tracking status updates.")
@app_commands.describe(milestone="Select the tracking update you want explained")
@app_commands.choices(milestone=[
    app_commands.Choice(name="Handed over to Airline / Departed", value="airline"),
    app_commands.Choice(name="Inbound Customs / Retained", value="customs"),
    app_commands.Choice(name="Arrived at Sorting Hub", value="hub")
])
async def status(interaction: discord.Interaction, milestone: app_commands.Choice[str]):
    embed = discord.Embed(title=f"🔍 Tracking Breakdown: {milestone.name}", color=0x34495E)
    if milestone.value == "airline":
        embed.description = "✈️ What it means: Your package has passed physical security checks and is loaded on an airplane or currently mid-flight over the ocean. It will not update again until it lands in your home country!"
    elif milestone.value == "customs":
        embed.description = "🛃 What it means: Your parcel is being scanned by border control agents. This is 100% normal. Most packages are processed and released automatically within 24 to 72 hours."
    elif milestone.value == "hub":
        embed.description = "🏢 What it means: Your parcel has reached a regional transport warehouse facility. It is being sorted into a delivery truck heading directly to your local area zip code."
    await interaction.response.send_message(embed=embed)

# Core Execution Runtime Block
async def main():
    await start_web_server()
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
