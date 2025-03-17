from supabase import create_client
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Conexión a Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
