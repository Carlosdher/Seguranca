from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode

def Chaves (tamanho):
	gerador = Random.new().read
	key = RSA.generate(tamanho, gerador)
	private = key
	public = key.PublicKey
	return private, public

def encrypt(mensagem, chave_publica):
	cipher = PKCS1_OAEP.new(chave_publica)
	return cipher.encrypt(mensagem) 

def decrypt(mensagem, chave_privada):
	cipher = PKCS1_OAEP.new(chave_privada)
	return cipher.decrypt(mensagem)