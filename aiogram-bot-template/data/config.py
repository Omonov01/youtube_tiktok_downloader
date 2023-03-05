from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxat
IP = env.str("ip")  # Xosting ip manzili
BOT_LINKS = "@sehrgar_bot"

DB_CONNECTION_URL = "postgresql://postgres:4wnzB0ekmbUf3xaFIq58@containers-us-west-151.railway.app:6735/railway"
# PGHOST = env.str("containers-us-west-151.railway.app")
# PGPORT = env.str("6735")
# PGUSER = env.str("postgres")
# PGPASSWORD = env.str("4wnzB0ekmbUf3xaFIq58")
# PGDATABASE = env.str("railway")
# DATABASE_URL = env.str("postgresql://${{ PGUSER }}:${{ PGPASSWORD }}@${{ PGHOST }}:${{ PGPORT }}/${{ PGDATABASE }}")



