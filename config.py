API_TOKEN = None
MY_ID = None
DB_FILENAME = 'vacres.db'

'''
@dp.message_handler(content_types=['photo'])
async def upload_photo(message: types.Message):
    logging.info(f'Started processing {message.photo[-1]}')
    file_id = message.photo[-1].file_id

    session = Session()
    newItem = MediaIds(file_id=file_id, filename=filename)
    try:
        session.add(newItem)
        session.commit()
    except Exception as e:
        logging.error(
            'Couldn\'t upload {}. Error is {}'.format(filename, e))
    else:
        logging.info(
            f'Successfully uploaded and saved to DB file {filename} with id {file_id}')
    finally:
        session.close()

'''

'''
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
'''