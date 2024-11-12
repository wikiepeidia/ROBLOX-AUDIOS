# ROBLOX-AUDIOS
Repository for experimenting with ROBLOX audios, especially after the Privacy update
## EXCEL FILE
- An EXCEL file has been added for convenience.
- Column A: add your song IDs, usually found by their name, ensure the format is SONGNAME+ID.
- Copy IDs in a COLUMN, not a single cell.
- Column E: will remove the text.
- You can hide Column A to avoid spoiling the music names.
- When adding new music, always add in Column A, and drag the box of Column E down.
- Column G: shuffled IDs. Use SORTBY (e.g E1:E10) to display 10 numbers in G column, and RANDARRAY (e.g E1:E10) to shuffle the range of numbers.
![image](https://github.com/user-attachments/assets/1f4bf423-bd37-4f26-90a5-7a069c96bf4c)

## PYTHON FILE
- A PYTHON file is for converting ID-->for the LUA FILE.
- Copy the ID in the G column in the EXCEL file, paste in name.txt file (COLUMN, PURE ID ONLY).
- Put the name.txt and the PYTHON file in the same folder.
- Run the python FILE. Remember to CD in CMD.
- Open the new file output.txt, copy the content into local soundid={}, check for any ERRORS.
![image](https://github.com/user-attachments/assets/e9f6458e-3ceb-4296-ba17-f96ea12ffb52)
![image](https://github.com/user-attachments/assets/eb185682-44b0-4f63-afd0-f9ecb28e4294)
![image](https://github.com/user-attachments/assets/ceff1041-c8de-492e-a595-2721af8845f4)

## LUA FILE
- Put the given script in WORKSPACE. It will replace ALL audios with your purposed ID.
- Make sure to setup YOUR ID!
![image](https://github.com/user-attachments/assets/13159abb-1b1d-46ce-b5c5-01a4042013f7)

## WARNING
- THIS SCRIPT IS FOR EDUCATIONAL PURPOSES. IF YOU PUT IT IN ANY GAME, IT WILL DESTROY IT.
- CONSEQUENCES: LOUD audios (A NON-LOUD IDS but played LOOPED in multiple times, best case is from GUNS when you need to SHOOT BULLETS in a short time), OVERLAPPING audios causing HUGE FPS DROPS!

## SOURCE:
- CHATGPT.
