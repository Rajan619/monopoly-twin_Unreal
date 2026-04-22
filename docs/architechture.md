# Architecture Overview

## High-Level Components

1. Vision System
2. State Manager
3. Networking Layer
4. Unreal Client

Each component is independently replaceable.

---

## Design Philosophy

### 1. Separation of Concerns

Vision does NOT know about Unreal.
Unreal does NOT know about OpenCV.

### 2. Event-Driven System

All updates are triggered via events:

* Pawn moved
* Dice rolled
* Player updated

### 3. Real-Time Constraints

* Low latency (<100ms target)
* Non-blocking processing
* Async communication

---

## Data Flow

1. Camera captures board
2. Vision detects pawn position
3. Position mapped to board index
4. State updated
5. WebSocket broadcasts update
6. Unreal reflects change

---

## Failure Handling

* Detection failure → ignore frame
* Network drop → reconnect logic
* Unreal desync → full state sync fallback
