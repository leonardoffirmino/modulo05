import uuid 
import qrcode

class Pix():
  def __init__(self):
    pass

  def create_payment(self,base_dir=""):
    #Criar pagamento na instituição financeira para gerar esse token para dar a notificação do pagamento.
    bank_payment_id = str(uuid.uuid4())

    #QrCode
    hash_payment = f'hash_payment_{bank_payment_id}'

    img = qrcode.make(hash_payment)
    img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")

    return{
      "bank_payment_id":bank_payment_id,
      "qr_code":f"qr_code_payment_{bank_payment_id}"
      }