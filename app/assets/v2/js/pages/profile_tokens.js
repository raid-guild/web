// Personal token constants
// Note that this address is also duplicated in board.js
const factoryAddress = '0x589C95378793DA00da5493b7D11145bb7991b682';
const purchaseTokenName = 'DAI';

$(document).on('click', '#submit_buy_token', (event) => {
  event.preventDefault();
  const form = $('#ptokenBuyForm')[0];

  if (form.checkValidity() === false) {
    event.stopPropagation();
    _alert('You must agree before submitting', 'error', 2000);
    return;
  }

  buyPToken($('#ptokenAmount').val());
});

$(document).on('input', '#ptokenRedeemAmount', (event) => {
  event.preventDefault();
  const amount = $(event.target).val();

  $('#ptokenRedeemCost').text(`${document.current_ptoken_value * parseFloat(amount) || 0} ${purchaseTokenName}`);
  $('#redeem-amount').text(parseFloat(amount));
});

$(document).on('input', '#ptokenAmount', (event) => {
  event.preventDefault();
  const amount = $(event.target).val();

  $('#ptokenCost').text(`${document.current_ptoken_value * parseFloat(amount) || 0} ${purchaseTokenName}`);
  $('#buy-amount').text(amount);
});

$(document).on('click', '#submit_redeem_token', (event) => {
  event.preventDefault();
  const form = $('#ptokenRedeemForm')[0];
  const amountField = $(form.ptokenRedeemAmount);
  const tos = $(form.ptokenRedeemTerms);
  const redeem_amount = parseFloat(amountField.val());

  if (!tos.prop('checked')) {
    event.stopPropagation();
    _alert('You must agree before submitting', 'error', 2000);
    tos.addClass('is-invalid');
    return;
  }
  tos.removeClass('is-invalid');

  if (isNaN(redeem_amount)) {
    _alert(`Provide a valid amount no greater than ${document.current_hodling} ${document.current_ptoken_symbol}`, 'error', 2000);
    amountField.addClass('is-invalid');
    return;
  } else if (document.current_hodling === 0) {
    _alert(`You don't have ${document.current_ptoken_symbol} tokens`, 'error', 2000);
    amountField.addClass('is-invalid');
    return;
  } else if (redeem_amount > document.current_hodling) {
    _alert(`You can't redeem more than ${document.current_hodling}  ${document.current_ptoken_symbol}`, 'error', 2000);
    amountField.addClass('is-invalid');
    return;
  }
  amountField.removeClass('is-invalid');

  redeemPToken($('#ptokenRedeemAmount').val());
});

async function buyPToken(tokenAmount) {
  // Make sure user is connected and request token approval
  const { user, purchaseTokenAddress } = await this.checkWeb3();
  const purchaseTokenContract = new web3.eth.Contract(token_abi, purchaseTokenAddress);
  const amount = web3.utils.toWei(tokenAmount);

  const pTokenAddress = undefined; // TODO

  purchaseTokenContract.methods.approve(pTokenAddress, amount);
  return;


  const pToken = await new web3.eth.Contract(
    document.contxt.ptoken_abi, // TODO: contxt.ptoken_abi needs to be implemented.
    pTokenAddress // TODO: this needs to be derived from the profile page
  );

  // Approve ptoken contract to spend your Dai

  pToken.methods
    .purchase(tokenAmount)
    .send({
      from: user
    })
    .on('transactionHash', function(transactionHash) {
      purchase_ptoken(
        tokenId, // TODO: determine token ID based on profile
        tokenAmount,
        user,
        (new Date()).toISOString(),
        transactionHash
      );
      // TODO need to confirm that transaction was confirmed. Use web3's getTransactionReceipt
    });
}

async function redeemPToken(tokenAmount) {
  // TODO this should be a redemption request with no web3, only DB update
  [user] = await web3.eth.getAccounts();
  const pToken = await new web3.eth.Contract(
    document.contxt.ptoken_abi, // TODO: contxt.ptoken_abi needs to be implemented.
    pTokenAddress // TODO: this needs to be derived from the profile page
  );

  pToken.methods
    .redeem(tokenAmount)
    .send({
      from: user
    })
    .on('transactionHash', function(transactionHash) {
      request_redemption(pTokenId, tokenAmount, network); // TODO: determine token ID and network
    });
  // TODO need to confirm that transaction was confirmed. Use web3's getTransactionReceipt
}

function handleError(err) {
  console.error(err); // eslint-disable-line no-console
  let message = 'There was an error';

  if (err.message)
    message = err.message;
  else if (err.msg)
    message = err.msg;
  else if (typeof err === 'string')
    message = err;

  _alert(message, 'error');
  indicateMetamaskPopup(true);
}

async function checkWeb3() {
  if (!web3) {
    _alert('Please connect a wallet', 'error');
    throw new Error('Please connect a wallet');
  }
  [user] = await web3.eth.getAccounts();

  if (document.web3network === 'rinkeby') {
    purchaseTokenAddress = '0x6A9865aDE2B6207dAAC49f8bCba9705dEB0B0e6D';
  } else if (document.web3network === 'mainnet') {
    purchaseTokenAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F';
  } else {
    _alert('Unsupported network', 'error');
    throw new Error('Please connect a wallet');
  }

  return { user, purchaseTokenAddress };
}
