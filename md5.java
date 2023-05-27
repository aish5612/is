import java.math.BigInteger;  
import java.security.MessageDigest;  
import java.security.NoSuchAlgorithmException;  
public class md5 
{  
//hash function to get the md5 hash  
public static String getMd5Hash(String input)  
{  
try   
{  
//static getInstance() method is called with hashing MD5  
MessageDigest md = MessageDigest.getInstance("MD5");  
//calculating message digest of an input that return array of byte  
byte[] messageDigest = md.digest(input.getBytes());  
//converting byte array into signum representation  
BigInteger no = new BigInteger(1, messageDigest);  
//converting message digest into hex value  
String hashtext = no.toString(16);  
while (hashtext.length() < 32)   
{  
hashtext = "0" + hashtext;  
}  
return hashtext;  
}  
//for specifying wrong message digest algorithms  
catch (NoSuchAlgorithmException e)   
{  
throw new RuntimeException(e);  
}  
}  
//driver code  
public static void main(String args[]) throws NoSuchAlgorithmException  
{  
String s = "javatpoint";  
System.out.println("HashCode Generated for the string is: " + getMd5Hash(s));  
}  
}  











#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

void calculate_md5_hash(const char* message, unsigned char* hash) {
    MD5_CTX md5_context;
    MD5_Init(&md5_context);
    MD5_Update(&md5_context, message, strlen(message));
    MD5_Final(hash, &md5_context);
}

int main() {
    const char* message = "Hello, MD5!";
    unsigned char hash[MD5_DIGEST_LENGTH];

    calculate_md5_hash(message, hash);

    printf("Original message: %s\n", message);
    printf("MD5 hash value: ");
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");

    return 0;
}
