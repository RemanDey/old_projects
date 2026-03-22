from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server(horizon_url="https://horizon-testnet.stellar.org")
source = Keypair.from_secret("SAUMECBXDG23VHNROCJM3US6NI2ZWATMJMXKSJSTE5BXSRINEG4VL5XG")
destination = Keypair.from_raw_ed25519_public_key("GDFEBTGAZ3CYHPGKWQJ26XMLHXKAHJS6IKEZMKWRTHRMMVILGKJ4PRGF")


source_account = server.load_account(account_id=source.public_key)
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_create_account_op(
        destination=destination.public_key, starting_balance="12.25"
    )
    .set_timeout(30)
    .build()
)
transaction.sign(source)
response = server.submit_transaction(transaction)
print(f"Transaction hash: {response['hash']}")
print(
    f"New Keypair: \n\taccount id: {destination.public_key}\n\tsecret seed: {destination.secret}"
)