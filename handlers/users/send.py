from aiogram import types
from loader import dp
from converter import converterr
import cloudconvert
@dp.message_handler(types=['video'])
async def test(message:types.Message):
    natija = converterr(message.video)
    if type(natija) is dict:
        exported_url_task_id = natija['id']
        res = cloudconvert.Task.wait(id=exported_url_task_id)  # Wait for job completion
        file = res.get("result").get("files")[0]
        res = cloudconvert.download(filename=file['filename'], url=file['url'])
        await message.answer_video(res)
    else:await message.answer("Bu manzil orqali hech narsa topilmadi")
