pragma solidity ^0.5.0;

import "./CosmoCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";


// Have the CosmoCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract CosmoCoinCrowdsale is Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundableCrowdsale { // UPDATE THE CONTRACT SIGNATURE TO ADD INHERITANCE
    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate, // rate in TKNbits
        address payable wallet, // sale beneficiary
        CosmoCoin token, // the CosmoCoin itself that the CosmoCoinCrowdsale will work with
        uint goal, // the crowdsale goal
        uint open, // the crowdsale opening time
        uint close // the crowdsale closing time
    ) public 
        Crowdsale(rate, wallet, token)
        CappedCrowdsale(goal)
        TimedCrowdsale(open, close)
        RefundableCrowdsale(goal)
    {
        // constructor can stay empty
    }
}

contract CosmoCoinCrowdsaleDeployer {
    // Create an `address public` variable called `cosmo_token_address`.
     address public cosmo_token_address;
    // Create an `address public` variable called `cosmo_crowdsale_address`.
    address public cosmo_crowdsale_address;

    // Add the constructor.
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet,
        uint initial_supply,
        uint goal
    ) public {
        // Create a new instance of the CosmoCoin contract.
        CosmoCoin token = new CosmoCoin(name, symbol, initial_supply);
        
        // Assign the token contract’s address to the `cosmo_token_address` variable.
        cosmo_token_address = address(token);

        // Create a new instance of the `CosmoCoinCrowdsale` contract
        CosmoCoinCrowdsale cosmo_crowdsale = new CosmoCoinCrowdsale (1, wallet, token, goal, now, now + 24 weeks);
            
        // Aassign the `CosmoCoinCrowdsale` contract’s address to the `cosmo_crowdsale_address` variable.
        cosmo_crowdsale_address = address(cosmo_crowdsale);

        // Set the `CosmoCoinCrowdsale` contract as a minter
        token.addMinter(cosmo_crowdsale_address);
        
        // Have the `CosmoCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}
