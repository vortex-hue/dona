import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.models import Payment
from xrpl.wallet import Wallet
from xrpl.constants import CryptoAlgorithm

def make_xrp_payment(sender_seed_or_wallet, xrp_amount):
    try:
        # Initialize an XRPL client
        xrpl_client = JsonRpcClient('https://s.altnet.rippletest.net:51234')  # Adjust to your XRPL server

        # Ensure sender_wallet is a Wallet instance
        if isinstance(sender_seed_or_wallet, str):
            # Create a Wallet instance using the provided seed
            sender_wallet = Wallet.from_seed(sender_seed_or_wallet)

        # Create a Payment transaction
        transaction = Payment(
            account=sender_wallet.address,
            amount=str(xrp_amount),  # Amount to send
            destination='rpvMAt53t4L3oQs7Ko9BDEZD9i7rgBqm2y',  # Use the recipient's XRP address
        )

        # Sign the transaction with the sender's wallet
        signed_transaction = xrpl.transaction.autofill_and_sign(transaction,xrpl_client,sender_wallet)
            
        # Submit the transaction to the XRP Ledger
        try:
            response = xrpl.transaction.submit_and_wait(signed_transaction, xrpl_client)
        except xrpl.transaction.XRPLReliableSubmissionException as e:
            exit(f"Submit failed: {e}")

        if response.is_successful():
            return signed_transaction.get_hash()  # Return the transaction hash
        else:
            return None

    except Exception as e:
        print(f"Error making XRP payment: {str(e)}")
        return None
