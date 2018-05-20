# Zadání

Dostali jste několik souborů, které jsou šifrovány neznámou synchronní proudovou šifrou. Vašim cílem je zjistit tajemství, 
které má formát KRY{24 znaků ASCII textu}. Programovací jazyk pro vypracování je Python 3. Odevzdvávejte archiv xlogin00.zip. 
Archiv bude obsahovat solution.py (soubor s obsahem ručního řešení), solution_sat.py (soubor s obsahem sat řešení), 
doc.pdf (dokumentace) a volitelně install.sh (pro automatickou instalaci závislostí). Skripty po spuštění vypíší na 
stdout tajemství. Skripty budou pracovat se sloužkou in, ve které bude rozbalený obsah archivu zadání (neodevzdávejte) 
a bude zjišťovat tajemství ze souborů v této složce šifrované zadanou šifrou. Pokud skript potřebuje závislosti, musí si je 
automaticky doinstalovat pomocí install.sh (install.sh bude spuštěn před spuštěním testu). Program vypíše tajemství na stdout 
a skončí. Vaše řešení bude testováno na Ubuntu 16.04, kernel 4.4.0-116.

V druhé části zadaní získejte tajemství pomocí SAT solveru aplikovaného na spravnou část šifry.
