#!/bin/sh
curl -X POST localhost:8080/memq/server/queues/bitcoin/drain
curl -X POST localhost:8080/memq/server/queues/bitcoin2/drain

