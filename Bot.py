from discord.ext import commands
import Currency
import LiveMarket



client = commands.Bot(command_prefix = '$', case_insensitive = True)

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user.name))

@client.command()
async def Rates(ctx):
    market = LiveMarket.API()
    rates = market.request('USD')

    parsedRates = str()
    currency = Currency.Utility()

    parsedRates += '%s %s is the base currency\n' % (currency.getFlagEmoji('USD'), currency.getFullName('USD'))
    for key in rates:
        flag = currency.getFlagEmoji(key)
        fullname = currency.getFullName(key)
        parsedRates += '%s %s[%s] - %.4f \n' % (flag, fullname, key, rates[key])

    await ctx.send(parsedRates)

@client.command()
async def Convert(ctx, *args):
    if len(args) != 4:
        await ctx.send('Invalid number of arguments')
        return

    fromCurrency = args[1].upper()
    toCurrency = args[3].upper()
    amount = args[0]

    if not amount.isnumeric():
        await ctx.send('Amount must be numeric')
        return

    amount = float(amount)
    currency = Currency.Utility()

    if not currency.exist(fromCurrency.upper()) or not currency.exist(toCurrency.upper()):
        await ctx.send('One or more currency is not supported')
        return

    market = LiveMarket.API()
    rates = market.request(fromCurrency)
    if toCurrency in rates:
        rate = float(rates[toCurrency])
        await ctx.send('%.2f %s to %s = %.2f' % (amount, fromCurrency, toCurrency, rate * amount))

fin = open('Files/Token', 'r')
client.run(fin.read())
