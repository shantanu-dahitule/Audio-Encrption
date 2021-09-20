from cryptography.fernet import Fernet

key = Fernet.generate_key()
audioFile=r'G:\VIT STUDY DOCS\Year 2021-22\Fall Semester 2021-22\Watermarking and Stegnography\projectData\BCI3005-main\App\Database\BCI_DATABASE_01.mp3'
fernet = Fernet(key)
# Encryption
with open('key.key','wb') as filekey:
    filekey.write(key)
with open ('key.key','rb') as filekey:
    key=filekey.read()
with open(audioFile, 'rb') as file:
    originalaudio=file.read()
encrypted=fernet.encrypt(originalaudio)
with open('encrypted voice.mp3','wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Decryption
fernet=Fernet(key)
encryptedaudioPath=r'G:\VIT STUDY DOCS\Year 2021-22\Fall Semester 2021-22\Watermarking and Stegnography\projectData\BCI3005-main\App\encrypted voice.mp3'
with open(encryptedaudioPath,'rb') as enc_file:
    encrypted=enc_file.read()
decrypted=fernet.decrypt(encrypted)
with open('Decrypted audio.mp3','wb') as dec_file:
    dec_file.write(decrypted)