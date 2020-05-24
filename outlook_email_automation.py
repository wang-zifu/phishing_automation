import imapclient
import pyzmail


def connect_email_info():
    """
    Get Exchange account connection with server
    """
    imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
    imapObj.login(' test@hotmail.com ', ' Password ')
    imapObj.select_folder('INBOX', readonly=True)


    unique_ids = []
    UIDs = imapObj.search(['ALL'])
    for IDs in UIDs:
        unique_ids.append(IDs)
    # print(unique_ids)
    message_id = unique_ids
    # print(message_id)

    rawMessages = imapObj.fetch(message_id, ['BODY[]', 'FLAGS'])
    
    email_ids = 0
    for email_ids in rawMessages:
        message = pyzmail.PyzMessage.factory(rawMessages[email_ids][b'BODY[]'])
        print("\n===============================================================")
        print("******Messages from INBOX folder separated with this lines*****")
        print("===============================================================\n")
        print(f"\nFrom: {message.get_addresses('from')}\n")
        print(f"To: {message.get_addresses('to')}\n")
        print(f"Subject: {message.get_subject()}\n")
        print(message)
    
    
def main():
    
    connect_email_info()
    
if __name__ == '__main__':
    main()

# import imaplib
# import email


# def read_email_from_outlook():
#         mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
#         mail.login('koguname@hotmail.com','61577Oguname')
#         mail.select('inbox')

#         result, data = mail.search(None, 'ALL')
#         mail_ids = data[0]

#         id_list = mail_ids.split()   
#         first_email_id = int(id_list[0])
#         latest_email_id = int(id_list[-1])

#         for i in range(latest_email_id,first_email_id, -1):
#             # need str(i)
#             result, data = mail.fetch(str(i), '(RFC822)' )

#             for response_part in data:
#                 if isinstance(response_part, tuple):
#                     # from_bytes, not from_string
#                     msg = email.message_from_bytes(response_part[1])
#                     email_subject = msg['subject']
#                     email_from = msg['from']
#                     email_to = msg['to']
                    
#                     print ('From : ' + email_from + '\n')
#                     print ('To : ' + email_to + '\n')
#                     print ('Subject : ' + email_subject + '\n')

# # nothing to print here
# read_email_from_outlook()