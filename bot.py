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
        bot.tree.copy_global_to(guild=GUILD_ID)
        synced = await bot.tree.sync(guild=GUILD_ID)
        await ctx.send(f"Successfully registered {len(synced)} slash commands directly to this server!")
    except Exception as e:
        await ctx.send(f"Sync failed: {e}")

@bot.tree.command(name="prohibited", description="Check standard international logistics shipping guidelines.")
@app_commands.describe(category="Select the logistics category to check general shipping rules")
@app_commands.choices(category=[
    app_commands.Choice(name="Apparel", value="apparel"),
    app_commands.Choice(name="Bags & Luggage", value="bags"),
    app_commands.Choice(name="Electronics", value="electronics"),
    app_commands.Choice(name="Cosmetics", value="cosmetics"),
    app_commands.Choice(name="Food Items", value="food"),
    app_commands.Choice(name="Toys & Models", value="toys"),
    app_commands.Choice(name="Printed Material", value="books")
])
async def prohibited(interaction: discord.Interaction, category: app_commands.Choice[str]):
    embed = discord.Embed(title=f"📋 Logistics Guideline Matrix: {category.name}", color=0xFFCC00)
    if category.value == "apparel":
        embed.add_field(name="🟢 Standard Route Items", value="Standard everyday fabrics, unbranded clothing, and basic cotton textiles.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Items requiring specific packaging adjustments based on weight or thickness parameters.", inline=False)
        embed.add_field(name="❌ Restricted/Banned", value="Wet garments, hazardous industrial fabrics, or items failing standard carrier safety guidelines.", inline=False)
    elif category.value == "bags":
        embed.add_field(name="🟢 Standard Route Items", value="Canvas backpacks, unbranded nylon pouches, basic travel luggage packages.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Bags with heavy metal ornaments or rigid structures that impact packing density.", inline=False)
        embed.add_field(name="❌ Restricted/Banned", value="Luggage carrying integrated power banks or unverified internal electronic battery compartments.", inline=False)
    elif category.value == "electronics":
        embed.add_field(name="🟢 Standard Route Items", value="Simple data cables, basic hardware panels, and non-battery accessories.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Devices with built-in lithium batteries or wireless network broadcasting components.", inline=False)
        embed.add_field(name="❌ Restricted/Banned", value="Loose standalone power banks, hazardous raw cells, or uncertified electrical hardware.", inline=False)
    elif category.value == "cosmetics":
        embed.add_field(name="🟢 Standard Route Items", value="Solid makeup applications, brushes, dry synthetic sponges, and clean tools.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Liquid products, setting sprays, dense creams, and fine loose cosmetic powders.", inline=False)
        embed.add_field(name="❌ Restricted/Banned", value="Flammable pressurized aerosol cans or unverified industrial chemical compounds.", inline=False)
    elif category.value == "food":
        embed.add_field(name="🟢 Standard Route Items", value="Completely sealed, shelf-stable commercial dry goods and crisp snack biscuits.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Vacuum-sealed localized dry tea leaves or dry regional cooking spices.", inline=False)
        embed.add_field(name="❌ Banned Items", value="Perishable raw meats, fresh produce, and unverified medical formulations.", inline=False)
    elif category.value == "toys":
        embed.add_field(name="🟢 Standard Route Items", value="Standard plastic interlocking building bricks, standard models, and clean plush dolls.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Remote control models containing wired circuitry elements or integrated magnets.", inline=False)
        embed.add_field(name="❌ Banned Items", value="Logistics-banned replica weapon models or uncertified toxic fluid toy accessories.", inline=False)
    elif category.value == "books":
        embed.add_field(name="🟢 Standard Route Items", value="Standard print publications, commercial catalogs, and non-restricted paperbacks.", inline=False)
        embed.add_field(name="⚠️ Specialized Cargo Notes", value="Heavy volume publication collection binders subject to line weight limits.", inline=False)
        embed.add_field(name="❌ Banned Items", value="Materials violating carrier shipping transport rules or destination entry regulations.", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="coupons", description="View platform registration rewards.")
async def coupons(interaction: discord.Interaction):
    embed = discord.Embed(title="🎁 LoloBuy Welcome Package & Rewards", color=0x2ECC71)
    embed.description = (
        "New users can claim their platform registration gifts upon signing up:\n\n"
        "• **15% OFF** Shipping Coupon\n"
        "• **10% OFF** Secondary Weight Coupon\n"
        "• **$500 Coupon Bundle** for warehouse operations!\n\n"
        "👉 [Click here to register your account and activate rewards!](https://lolobuy.com)"
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="convert", description="Convert Chinese Yuan (CNY) to international baseline metrics.")
@app_commands.describe(cny="The cost value in Chinese Yuan (e.g. 500)")
async def convert(interaction: discord.Interaction, cny: float):
    usd = cny * 0.14
    eur = cny * 0.13
    gbp = cny * 0.11
    embed = discord.Embed(title="💱 CNY Reference Conversion Card", color=0x3498DB)
    embed.add_field(name="🇨🇳 Chinese Yuan", value=f"**{cny:.2f} CNY**", inline=False)
    embed.add_field(name="🇺🇸 US Dollar (Ref)", value=f"${usd:.2f} USD", inline=True)
    embed.add_field(name="🇪🇺 Euro (Ref)", value=f"€{eur:.2f} EUR", inline=True)
    embed.add_field(name="🇬🇧 British Pound (Ref)", value=f"£{gbp:.2f} GBP", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="yupoo", description="Informational guide regarding standard marketplace engine link formatting.")
async def yupoo(interaction: discord.Interaction):
    embed = discord.Embed(title="📸 Marketplace Link Information Guide", color=0x9B59B6)
    embed.description = (
        "When submitting order entries into the LoloBuy system layout:\n\n"
        "1. Ensure you extract the active checkout item links provided by sellers.\n"
        "2. Paste standard store links into the dashboard routing tool.\n\n"
        "⚠️ **Logistics Note:** The LoloBuy search field handles standard direct checkout catalog links (such as **Weidian, Taobao, or 1688** URLs). Ensure you submit compatible destination links during ordering panels."
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="track", description="Learn how to monitor international waybills.")
async def track(interaction: discord.Interaction):
    embed = discord.Embed(title="📦 3-Step Parcel Tracking Portal Sequence", color=0x5DADE2)
    embed.add_field(name="Step 1: Get Code", value="Navigate to your LoloBuy profile dashboard order panel to check your tracking waybill code.", inline=False)
    embed.add_field(name="Step 2: Copy Code", value="Copy the unique alphanumeric routing sequence string provided for your order.", inline=False)
    embed.add_field(name="Step 3: Verification", value="Input the tracking string into public shipment checking sites like [17track](https://17track.net) for milestone updates.", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="estimator", description="Shipping Freight Cost Calculation Tutorial.")
async def estimator(interaction: discord.Interaction):
    embed = discord.Embed(title="⚖️ Shipping Freight & Volume Cost Estimation", color=0xE67E22)
    embed.description = (
        "Before finalizing parcel submissions, utilize the platform's cost tool:\n\n"
        "• Weight parameters are processed using volumetric mass or true scale values depending on line metrics.\n"
        "• Select your destination country network to view matching available lines.\n"
        "• Review approximate price speed tier differences on the official platform page before dispatch."
    )
    await interaction.response.send_message(embed=embed)

    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="rehearsal", description="Learn how Warehouse Rehearsal Packaging processes function.")
async def rehearsal(interaction: discord.Interaction):
    embed = discord.Embed(title="📦 Rehearsal Packaging Warehouse Process", color=0x1ABC9C)
    embed.description = (
        "Want to check your verified parcel dimensions upfront? You can opt for rehearsal metrics:\n\n"
        "• Warehouse logistics staff pre-pack your selected cart items into a real container box.\n"
        "• This determines the **physical dimensions and true weight metrics** ahead of final billing.\n"
        "• Helps you verify package profiles before submitting final courier choices."
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="lines", description="View standard shipping route information by region.")
@app_commands.describe(region="Select the geographic region to review available network formats")
@app_commands.choices(region=[
    app_commands.Choice(name="Europe (EU)", value="eu"),
    app_commands.Choice(name="United States & Canada (NA)", value="na"),
    app_commands.Choice(name="United Kingdom (UK)", value="uk")
])
async def lines(interaction: discord.Interaction, region: app_commands.Choice[str]):
    embed = discord.Embed(title=f"✈️ Shipping Network General Profiles: {region.name}", color=0x9B59B6)
    if region.value == "eu":
        embed.add_field(name="📦 DHL Logistics Routes", value="**General Speed:** 8-14 Days\n**Features:** Heavily utilized across continental Europe. Offers stable tracking data streams. Check the active shipping panel for live estimates.", inline=False)
    elif region.value == "na":
        embed.add_field(name="📦 EMS Route Types", value="**General Speed:** 7-12 Days\n**Features:** Regular shipping line tracking available across North America. Charged based on actual scale weight properties.", inline=False)
        embed.add_field(name="📦 Postal Line Options", value="**General Speed:** 12-18 Days\n**Features:** Standard carrier network processing, frequently useful for smaller package allocations under 2kg.", inline=False)
    elif region.value == "uk":
        embed.add_field(name="📦 Royal Mail Route Types", value="**General Speed:** 8-12 Days\n**Features:** Standard regional domestic network options providing reliable delivery handoffs across the UK region.", inline=False)
    embed.set_footer(text="Notice: Delivery speeds are estimates. Always consult the live platform calculator for up-to-date regional values.")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="volumetric", description="Calculate the volumetric package weight used by logistics lines.")
@app_commands.describe(length="Length of the box in cm", width="Width of the box in cm", height="Height of the box in cm")
async def volumetric(interaction: discord.Interaction, length: float, width: float, height: float):
    vol_weight = (length * width * height) / 5000
    embed = discord.Embed(title="📐 Volumetric Weight Estimation Matrix", color=0xE67E22)
    embed.description = (
        f"Box Dimensions: {length} x {width} x {height} cm\n\n"
        f"📊 Estimated Volumetric Weight: {vol_weight:.2f} kg\n\n"
        "⚠️ Logistics Note: International carriers process shipping freight bills using whichever metric is higher between the true physical weight and this volumetric calculation."
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="status", description="Decode confusing tracking status updates.")
@app_commands.describe(milestone="Select the tracking update you want explained")
@app_commands.choices(milestone=[
    app_commands.Choice(name="The instruction data for this shipment have been provided by the sender to DHL electronically", value="electronic"),
    app_commands.Choice(name="The flight landed, and the board was dismantled and cleared", value="landed"),
    app_commands.Choice(name="The goods have been picked up and are currently undergoing customs clearance", value="customs")
])
async def status(interaction: discord.Interaction, milestone: app_commands.Choice[str]):
    embed = discord.Embed(title=f"🔍 Tracking Breakdown: Update Explained", color=0x34495E)
    if milestone.value == "electronic":
        embed.add_field(
            name="📝 Instruction data provided electronically",
            value="What it means: The shipping label data has been logged into the logistics network system. The physical parcel is processing inside the outbound distribution center waiting for transportation vehicle handoffs. Normal processing time applies."
        )
    elif milestone.value == "landed":
        embed.add_field(
            name="🛬 The flight landed, and the board was dismantled and cleared",
            value="What it means: The transit vehicle carrying the batch has arrived at the destination airport facility. Ground crews have unbundled the bulk pallet frameworks and checking individual parcels into sorting hubs."
        )
    elif milestone.value == "customs":
        embed.add_field(
            name="🛃 The goods have been picked up and are currently undergoing customs clearance",
            value="What it means: The import lot is passing review checks conducted by localized regional customs authorities. This is a baseline requirement for international freight packages and typical sorting time frames apply."
        )
    embed.set_footer(text="This general breakdown applies to standard international shipping workflows.")
    await interaction.response.send_message(embed=embed)

async def main():
    await start_web_server()
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
