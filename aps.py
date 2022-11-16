import requests
import pandas as pd
from distutils.cmd import Command
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,USD-ARS,USD-BOB,USD-CLP,USD-COP,USD-PEN,USD-PYG,USD-UYU,USD-VEF")

requisicao_dic = requisicao.json()
cotacao_dolar = (requisicao_dic["USDBRL"]["bid"])
cotacao_argentino = (requisicao_dic["USDARS"]["bid"])
cotacao_bolivar = (requisicao_dic["USDBOB"]["bid"])
cotacao_chile = (requisicao_dic["USDCLP"]["bid"])
cotacao_colombia = (requisicao_dic["USDCOP"]["bid"])
cotacao_peru = (requisicao_dic["USDPEN"]["bid"])
cotacao_paraguai = (requisicao_dic["USDPYG"]["bid"])
cotacao_uruguai = (requisicao_dic["USDUYU"]["bid"])
cotacao_venezuela = (requisicao_dic["USDVEF"]["bid"])

bot = Client(
    'APS_bot',
    api_id=24149393,
    api_hash="d6a78b3ba9034befb395eda2e3bc7fc4",
    bot_token="5724084576:AAFpv0u_o42fTCPDhkmwmXA2a2lNckrHSoU"
)

@bot.on_message(filters.sticker | filters.photo)
async def sticker(client, message):
    await message.reply('**Foto ou figurinha? vish prefiro mensagem mesmo**')
    
@bot.on_message(filters.voice)
async def voie(client, message):
    await message.reply('**Desculpe não consigo ouvir nada**')
    
@bot.on_message(filters.command('Brasil'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://images.pexels.com/photos/6321080/pexels-photo-6321080.jpeg?auto=compress&cs=tinysrgb&w=600')
    await message.reply('**A imagem acima representa a bandeira do Brasil,\nCapital: São paulos \nPopulação: 214 milhões (2021)**\n**Moeda: Real**\n**Valor da moeda: 1 dólar = **'+ cotacao_dolar + '**\n/Voltar**')
    
@bot.on_message(filters.command('Uruguai'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'http://geo5.net/imagens/2011/06/bandeira-do-uruguai-2000px-350x233.png')
    await message.reply('**A imagem acima representa a bandeira do Uruguai,\nCapital: Montevidéu \nPopulação: 3,48 milhões (2021)**\n**Moeda: Peso Uruguaio**\n**Valor da moeda: 1 dólar = **' + cotacao_uruguai + '**\n/Voltar**')
    
@bot.on_message(filters.command('Argentina'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://static.significados.com.br/foto/argentina.jpg')
    await message.reply('**A imagem acima representa a bandeira da Argentina,\nCapital: Buenos Aires \nPopulação: 45,81 milhões (2021)**\n**Moeda: Peso Argentino**\n**Valor da moeda: 1 dólar = **' + cotacao_argentino + '**\n/Voltar**')
    
@bot.on_message(filters.command('Chile'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://static.todamateria.com.br/upload/ba/nd/bandeiradochile-cke.jpg')
    await message.reply('**A imagem acima representa a bandeira do Chile,\nCapital: Santiago \nPopulação: 19,21 milhões (2021)**\n**Moeda: Peso Chileno**\n**Valor da moeda: 1 dólar = **' + cotacao_chile + '**\n/Voltar**')
    
@bot.on_message(filters.command('Bolivia'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://maestrovirtuale.com/wp-content/uploads/2019/10/bolivia-162245_6401.png')
    await message.reply('**A imagem acima representa a bandeira da Bolívia,\nCapital: La Paz \nPopulação: 11,83 milhões (2021)**\n**Moeda: Bolivares Bolivianos**\n**Valor da moeda: 1 dólar = **' + cotacao_bolivar + '**\n/Voltar**')
    
@bot.on_message(filters.command('Paraguai'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://static.todamateria.com.br/upload/pa/ra/paraguai.jpg')
    await message.reply('**A imagem acima representa a bandeira do Paraguai,\nCapital: Assunção \nPopulação: 7,22 milhões (2021)**\n**Moeda: Guarani Paraguaio**\n**Valor da moeda: 1 dólar = **' + cotacao_paraguai + '**\n/Voltar**')
    
@bot.on_message(filters.command('Peru'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/800px-Flag_of_Peru_%28state%29.svg.png')
    await message.reply('**A imagem acima representa a bandeira do Peru,\nCapital: Lima \nPopulação: 33 milhões (2021)**\n**Moeda: Novo Sol Peruano**\n**Valor da moeda: 1 dólar = '+ cotacao_peru + '**\n/Voltar**')

    
@bot.on_message(filters.command('Equador'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://maestrovirtuale.com/wp-content/uploads/2019/10/640px-Flag_of_Ecuador.svg_-1.png')
    await message.reply('**A imagem acima representa a bandeira do Equador,\nCapital: Quito \nPopulação: 17 milhões (2021)**\n**Moeda: Dólar Americano**\n**/Voltar**')
    
@bot.on_message(filters.command('Colombia'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://maestrovirtuale.com/wp-content/uploads/2019/10/bandera-colombia.jpg')
    await message.reply('**A imagem acima representa a bandeira da Colômbia,\nCapital: Bogotá \nPopulação: 51 milhões (2021)**\n**Moeda: Pesos Colômbianos**\n**Valor da moeda: 1 dólar = **' + cotacao_colombia + '**\n/Voltar**')
    await message.reply(cotacao_colombia)
    
@bot.on_message(filters.command('Venezuela'))
async def message(client, message):
    await bot.send_photo(message.chat.id, 'https://thumbs.dreamstime.com/z/bandeira-de-venezuela-50942480.jpg')
    await message.reply('**A imagem acima representa a bandeira da Venezuela,\nCapital: Caracas \nPopulação: 28 milhões (2021)**\n**Moeda: Bolivar Venezuelano**\n**Valor da moeda: 1 dólar = **' + cotacao_venezuela + '**\n/Voltar**')
    await message.reply(cotacao_venezuela)

    
@bot.on_message(filters.command('Equipe'))
async def message(client, message):
    await message.reply('**Denis de Sousa Rocha \nGabriel Henrique Selani Barbosa \nJeferson Gustavo Figueira \nJeferson Gustavo Figueira \nRuan Carlos Rocha Falcão \nYago Alan Cordeiro da Silva \n/voltar**')
    
@bot.on_message(filters.command('voltar'))
async def messages(client, message):
    await message.reply('**Olá bem vindo ao GeoBot o bot que te ensina um pouquinho mais sobre os paises 🌎, selecione uma das opções abaixo para conhecer mais sobre o país.**\n**/Brasil**\n**/Uruguai**\n**/Argentina**\n**/Chile**\n**/Bolivia**\n**/Paraguai**\n**/Peru**\n**/Equador**\n**/Colombia**\n**/Venezuela**\n**/Equipe**\n🌍')
    
@bot.on_message()
async def messages(client, message):
    await message.reply('**Olá bem vindo ao GeoBot o bot que te ensina um pouquinho mais sobre os paises 🌎, selecione uma das opções abaixo para conhecer mais sobre o país.**\n**/Brasil**\n**/Uruguai**\n**/Argentina**\n**/Chile**\n**/Bolivia**\n**/Paraguai**\n**/Peru**\n**/Equador**\n**/Colombia**\n**/Venezuela**\n**/Equipe**\n🌍')

bot.run()