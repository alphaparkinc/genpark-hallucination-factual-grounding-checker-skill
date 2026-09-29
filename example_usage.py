from client import GroundingChecker

src = "Kafka utilizes distributed commit logs partitioned across broker nodes with ZooKeeper/KRaft coordination."
c1 = "Kafka uses partitioned distributed commit logs on brokers."
c2 = "Kafka utilizes high-frequency quantum teleportation to send data."

print("Claim 1 Grounding:", GroundingChecker.evaluate(c1, src))
print("Claim 2 Grounding:", GroundingChecker.evaluate(c2, src))
