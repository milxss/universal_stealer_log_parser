**<h1> What is Stealer malware and how does it operate?</h1>** 
Stealer malware is a type of malware that is designed to steal sensitive information from infected systems. When executed, it typically searches for and collects data such as browser-saved login credentials, credit card information, browser history and cookies, cryptocurrency wallet access, desktop files, gaming credentials among other technical instance’s information and it even takes desktop screenshots.

This information is then sent back to the attacker’s command and control server, where it can be used for malicious purposes such as identity theft, financial fraud, or espionage. 

Stealer malware can be distributed through various means, including phishing emails, malicious websites, and infected software downloads. Once installed on a system, it can operate in the background without the user’s knowledge, collecting data and sending it back to the attacker.

**Most antivirus software can’t detect stealer malware.**

As a cyber security researcher I work with stealer malware logs on a daily basis, that's why I decided to facilitate my life and automate some of the processes.


# Universal stealer malware logs parser

**This tool is designed to retrieve all the compromised accounts and credit cards from stealer malware logs.
Made for cyber security educational purposes only.**

Currently supports:
- Racoon,
- StealC,
- RedLine,
- Aurora,
- Meta,
- Paranoid checker logs,
- CINOSHI stealer/botnet/clipper/miner,
- [EXPERTLOGS STEALER],
- other modified RedLine or Racoon family stealer malware. 

<img width="262" alt="Screenshot 2023-05-15 at 20 11 36" src="https://github.com/milxss/racoon_log_parser/assets/42537931/0552234b-ca21-42d4-bb24-c137e1b69d10"> <img width="462" alt="Screenshot 2023-05-15 at 20 11 15" src="https://github.com/milxss/racoon_log_parser/assets/42537931/f2a67bee-4c11-4fd2-8f4b-d58dd27ce74f">
<img width="364" alt="Screenshot 2023-05-18 at 00 02 40" src="https://github.com/milxss/racoon_log_parser/assets/42537931/1f6eee5d-ffbd-4943-b06e-b34c4820a4d8">
<img width="335" alt="Screenshot 2023-05-18 at 00 02 08" src="https://github.com/milxss/racoon_log_parser/assets/42537931/aa5379e3-099d-4175-8e57-9dba293de0b5">
<img width="338" alt="Screenshot 2023-05-18 at 00 01 21" src="https://github.com/milxss/racoon_log_parser/assets/42537931/be40d4ec-eba6-42ed-8b59-afe1f578bbd5">
<img width="375" alt="Screenshot 2023-06-12 at 15 41 10" src="https://github.com/milxss/universal_log_parser/assets/42537931/58150d1b-6da6-4609-8671-9ec58aae6b31">
<img width="369" alt="moon" src="https://github.com/milxss/universal_stealer_log_parser/assets/42537931/df81b5fd-7459-40e1-b4d8-b629c7326d84">
<img width="595" alt="Screenshot 2023-05-18 at 00 00 24" src="https://github.com/milxss/racoon_log_parser/assets/42537931/2c3eb768-883a-47ba-a201-d62b49b4ac8a">


**<h1> Disclaimer </h1>**
This log parser solution has been tested on UNIX systems only, Windows OS tests have not been conducted. 


**<h1> How to use it?</h1>**

1. To make it work simply run main.py. 
2. You will be asked to specify a main folder path, meaning a path to a folder where unpacked logs are situated. Example: Usr/milxss/logs
3. To thank me, you can star this GitHub repository <3
