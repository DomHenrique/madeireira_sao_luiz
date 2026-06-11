import os
import uuid
import unicodedata
from django.utils.deconstruct import deconstructible
from django.utils.text import get_valid_filename
from storages.backends.s3boto3 import S3Boto3Storage

@deconstructible
class SupabaseSafeS3Storage(S3Boto3Storage):
    """
    Storage customizado para o Supabase S3 que resolve problemas críticos:
    1. Erro 400 Bad Request em nomes de arquivos com espaços ou acentos.
    2. Garante nomes de arquivos únicos gerando um UUID, evitando colisões.
    """
    def get_valid_name(self, name):
        name = str(name)
        # Remove acentos
        name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
        
        dirname, filename = os.path.split(name)
        base, ext = os.path.splitext(filename)
        
        # Gera nome único para o arquivo (para evitar problemas de cache e overwrites)
        unique_filename = f"{uuid.uuid4().hex[:12]}{ext.lower()}"
        
        if dirname:
            return os.path.join(dirname, unique_filename).replace('\\', '/')
        return unique_filename
