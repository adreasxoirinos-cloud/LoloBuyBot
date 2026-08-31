import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = discord.Object(id=1543959901393391678)

# Configure bot intents
intents = discord.Intents.default()
intents.message_content = True

class LoloBuyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")
        print("Startup complete. Background global sync skipped to prevent Cloudflare Error 1015.")

bot = LoloBuyBot()

# Owner Only Sync Command
@bot.command(name="sync")
@commands.is_owner()
async def sync(ctx: commands.Context):
    """Copies global command tree matrix and registers it directly to the designated Guild ID."""
    await ctx.send("🔄 Copying command matrix to target Guild...")
    try:
        bot.tree.copy_global_to(guild=GUILD_ID)
        synced = await bot.tree.sync(guild=GUILD_ID)
        await ctx.send(f"✅ Successfully synced {len(synced)} slash commands to Guild {GUILD_ID.id} for instant rendering.")
    except Exception as e:
        await ctx.send(f"❌ Synchronization failed: {e}")

@sync.error
async def sync_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("❌ This setup utility is restricted exclusively to the bot owner.")

# /prohibited Slash Command
@bot.tree.command(name="prohibited", description="View DHL Compliance Logistics Manual guidelines.")
@app_commands.describe(category="Select an item category to view its transport rules.")
@app_commands.choices(category=[
    app_commands.Choice(name="Apparel", value="apparel"),
    app_commands.Choice(name="Bags/Luggage", value="bags"),
    app_commands.Choice(name="Electronics/Watches", value="electronics"),
    app_commands.Choice(name="Cosmetics", value="cosmetics"),
    app_commands.Choice(name="Food/Medicine", value="food"),
    app_commands.Choice(name="Toys", value="toys"),
    app_commands.Choice(name="Books/Adult Products", value="adult")
])
async def prohibited(interaction: discord.Interaction, category: app_commands.Choice[str]):
    embed = discord.Embed(
        title=f"📦 DHL Logistics Manual: {category.name}",
        description="Review logistics safety statuses before checking out.",
        color=discord.Color.orange()
    )
    
    if category.value == "apparel":
        embed.add_field(name="🟢 Transportable", value="Standard unbranded shirts, pants, and socks.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Luxury replicas or designer items (Requires specialized luxury lines).", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Items with hazardous built-in metal decorations.", inline=False)
    elif category.value == "bags":
        embed.add_field(name="🟢 Transportable", value="Canvas backpacks, un branded nylon wallets.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Branded leather bags (Requires specialized lines to bypass customs checks).", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Bags with large integrated powerbanks.", inline=False)
    elif category.value == "electronics":
        embed.add_field(name="🟢 Transportable", value="Passive wires, phone cases without electronic components.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Smartwatches, bluetooth earbuds, devices with built-in lithium batteries.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Loose lithium ion batteries, high-wattage power banks.", inline=False)
    elif category.value == "cosmetics":
        embed.add_field(name="🟢 Transportable", value="Solid beauty tools, makeup brushes, blending sponges.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Powders, lipsticks, standard creams (Specialized cosmetics line needed).", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Flammable liquids, nail polishes, aerosol sprays, perfumes.", inline=False)
    elif category.value == "food":
        embed.add_field(name="🟢 Transportable", value="None (Highly restricted across standard airmail networks).", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Sealed non-perishable snacks, tea leaves (Requires specialized food route).", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Raw meat, fresh fruits, liquid medicine, prescription drugs.", inline=False)
    elif category.value == "toys":
        embed.add_field(name="🟢 Transportable", value="Plushies, standard plastic building blocks.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Toys with small internal batteries or generic motors.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Magnetic balls, realistic toy weapons, liquids/slimes.", inline=False)
    elif category.value == "adult":
        embed.add_field(name="🟢 Transportable", value="Standard printed reference books, non-restricted literature.", inline=False)
        embed.add_field(name="⚠️ Sensitive/Restricted Cargo", value="Adult toys without batteries, specialized artistic catalogs.", inline=False)
        embed.add_field(name="❌ Banned for Transport", value="Political publications, religious propagation materials, battery adult items.", inline=False)
        
    await interaction.response.send_message(embed=embed)

# Command 2: /coupons
@bot.tree.command(name="coupons", description="View registration rewards and affiliate accelerator.")
async def coupons(interaction: discord.Interaction):
    embed = discord.Embed(title="🎁 LoloBuy Welcome Package & Rewards", color=0x2ECC71)
    embed.description = (
        "Join today and claim your platform registration gifts:\n\n"
        "• **15% OFF** Shipping Coupon\n"
        "• **10% OFF** Secondary Weight Coupon\n"
        "• **$500 Coupon Bundle** for new warehouse users!\n\n"
        "👉 [Click here to register your account and activate rewards!](https://www.lolobuy.com/index?inviteCode=antog1an)"
    )
    await interaction.response.send_message(embed=embed)

# /convert Slash Command
@bot.tree.command(name="convert", description="Convert Chinese Yuan (CNY) into major world currencies.")
@app_commands.describe(cny="The cost amount in Chinese Yuan (CNY) to convert.")
async def convert(interaction: discord.Interaction, cny: float):
    # Dummy conversion reference rates
    usd_rate = 0.14
    eur_rate = 0.13
    gbp_rate = 0.11
    
    usd_val = cny * usd_rate
    eur_val = cny * eur_rate
    gbp_val = cny * gbp_rate

    embed = discord.Embed(
        title="💱 Currency Conversion Results",
        description=f"Baseline Reference Conversion for **{cny:.2f} CNY**",
        color=discord.Color.blue()
    )
    embed.add_field(name="🇺🇸 US Dollars", value=f"${usd_val:,.2f}", inline=True)
    embed.add_field(name="🇪🇺 Euros", value=f"€{eur_val:,.2f}", inline=True)
    embed.add_field(name="🇬🇧 British Pounds", value=f"£{gbp_val:,.2f}", inline=True)
    await interaction.response.send_message(embed=embed)

# /yupoo Slash Command
@bot.tree.command(name="yupoo", description="View Yupoo Purchasing & Catalog Guide.")
async def yupoo(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📸 Yupoo Purchasing & Catalog Guide",
        description="How to safely browse and buy items from seller photo galleries.",
        color=discord.Color.purple()
    )
    embed.add_field(name="🔍 Browsing Galleries", value="Find your desired items inside seller galleries and extract the item descriptions/purchasing keys.", inline=False)
    embed.add_field(name="⚠️ Critical Warning", value="**NEVER paste yupoo.com links directly into the LoloBuy engine.** Doing so will cause order failures.", inline=False)
    embed.add_field(name="✅ Correct Method", value="Extract and supply valid marketplace URLs such as **Weidian**, **Taobao**, or **1688** links provided by the seller.", inline=False)
    await interaction.response.send_message(embed=embed)

# /track Slash Command
@bot.tree.command(name="track", description="View Parcel Tracking Portal Sequence.")
async def track(interaction: discord.Interaction):
    embed = discord.Embed(
        title="✈️ International Parcel Tracking Sequence",
        description="Follow these 3 simple steps to monitor your international waybills:",
        color=discord.Color.teal()
    )
    embed.add_field(name="1️⃣ Locate Tracking Code", value="Go to your LoloBuy order profile dashboard and find your assigned international waybill number.", inline=False)
    embed.add_field(name="2️⃣ Copy the Code", value="Copy the raw waybill alphanumerics without trailing spaces.", inline=False)
    embed.add_field(name="3️⃣ Track Globally", value="Paste the code into trusted tracking engines like [17track](https://www.17track.net) for real-time validation.", inline=False)
    await interaction.response.send_message(embed=embed)

# /estimator Slash Command
@bot.tree.command(name="estimator", description="View Shipping Cost Estimation Tool tutorial.")
async def estimator(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📐 Shipping Cost Estimation Guide",
        description="Understand how to calculate freight costs before purchasing.",
        color=discord.Color.blurple()
    )
    embed.add_field(name="📊 Freight Calculation", value="Shipping prices are determined using a mix of actual deadweight and volumetric sizing metrics.", inline=False)
    embed.add_field(name="⏱️ Weight Speeds", value="Fast air lines cost more per gram but deliver quickly, while sea/rail lines provide massive savings for heavy hauls.", inline=False)
    embed.add_field(name="💡 Strategy", value="Use the estimator tools on the platform to simulate your load weight *before* submitting marketplace orders.", inline=False)
    await interaction.response.send_message(embed=embed)

# /rehearsal Slash Command
@bot.tree.command(name="rehearsal", description="View Rehearsal Packaging Warehouse Utility instructions.")
async def rehearsal(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📦 Rehearsal Packaging Warehouse Utility",
        description="Learn how to pre-box your haul to save money up front.",
        color=discord.Color.gold()
    )
    embed.add_field(name="⚙️ Optimization Process", value="Warehouse staff pack your selected items together into a final box *before* you pay final shipping fees.", inline=False)
    embed.add_field(name="📏 True Dimensions & Sizing", value="This lets you acquire exact baseline weight dimensions and structural size metrics immediately.", inline=False)
    embed.add_field(name="💰 Bypass Adjustments", value="Using rehearsal packaging helps you avoid unexpected shipping overages or post-payment balance revisions.", inline=False)
    await interaction.response.send_message(embed=embed)

if __name__ == "__main__":
    if not TOKEN:
        print("Error: DISCORD_TOKEN is missing from your environment configuration.")
    else:
        # Run bot using unbuffered output for cleaner logs on cloud hosts like Render
        import sys
        sys.stdout.flush()
        bot.run(TOKEN)
