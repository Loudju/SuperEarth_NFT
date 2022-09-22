pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract StarRegistry is ERC721Full {
    constructor() public ERC721Full("StarRegistryToken", "STAR") {}

    struct Starland {
        string name;
        uint256 appraisalValue;
    }

    mapping(uint256 => Starland) public starlandCollection;

    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI);

    function registerStarland(
        address owner,
        string memory name,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        starlandCollection[tokenId] = Starland(name, initialAppraisalValue);

        return tokenId;
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        starlandCollection[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return starlandCollection[tokenId].appraisalValue;
    }
}
