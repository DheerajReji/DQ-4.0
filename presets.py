# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>നിങ്ങൾ ചോദിച്ച {} മൂവി ലഭിക്കാൻ താഴെ കാണുന്ന ബട്ടണിൽ ക്ലിക്ക് ചെയ്യുക</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<i>I can help you getting movies from</i> @OB_Movies "
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting Movies from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact Movie name.\n\n🔊 I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>Bot won't work in PM, Ask in ma Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>ചില സാങ്കേതിക തകരാറുകൾ മൂലം {} മൂവി ലഭ്യമല്ല 😞</b>\n<code>\n അൽപ്പസമയത്തിനു ശേഷം മൂവി ഒരു പ്രാവശ്യം കൂടി ചോദിക്കുക!</code>"
    MEDIA_SEND_TEXT = "<code>{} മൂവിയുടെ ഫയലുകൾ PM ൽ അയച്ചിട്ടുണ്ട്</code>"
    NO_MEDIA = "താഴെ ഉള്ള ബട്ടണിൽ ക്ലിക്ക് ചെയ്ത് ഗൂഗിളിൽ പോയി Correct Spelling കണ്ടുപിടിച്ച ശേഷം അത് കോപ്പി ചെയ്ത് ഇവിടെ Paste ചെയ്യുക"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
