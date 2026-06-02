# 404SkillNotFound

## Featured Projects

### 🔹 orderbook-engine
A C++ order book matching engine built to understand how markets work at a fundamental level — price-time priority, FIFO execution, partial fills, and order cancellation.

- Price levels stored in `std::map` for automatic sorted ordering; fast access to best bid and ask
- Per-level order queues in `std::list` for strict FIFO execution and efficient front removal
- Supports full and partial fills — unmatched remainder stays live in the book
- Benchmarked at ~1.3M orders/second (~757ns/order) on a 100k synthetic workload
- `addOrder()` avg ~35.6ms · `matchOrder()` avg ~24.0ms across benchmark runs

→ [404SkillNotFound/orderbook-engine](https://github.com/404SkillNotFound/orderbook-engine)

---

### 🔹 tiny-httpserver-cpp
A minimal HTTP/1.1 server written from scratch in C++ using raw sockets, built to explore low-level networking and I/O handling.

- Socket programming and TCP fundamentals
- Basic HTTP request parsing
- Minimal, readable architecture focused on learning

→ [404SkillNotFound/tiny-httpserver-cpp](https://github.com/404SkillNotFound/tiny-httpserver-cpp)

---

## About

I focus on **C++ and performance-oriented programming**, with an emphasis on algorithms, memory management, and system-level design.

This profile is a curated log of projects, experiments, and ongoing technical exploration. The goal is to build things from scratch, understand the internals, and iterate toward correctness before optimisation.

Current interests: matching engines, networking, low-latency systems.
