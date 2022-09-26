pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract Certificate is ERC721Full {
    constructor() public ERC721Full("LandToken", "LAND") {}

    function purchaseLand(address buyer, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newLandId = totalSupply();
        _mint(buyer, newLandId);
        _setTokenURI(newLandId, tokenURI);

        return newLandId;
    }
}