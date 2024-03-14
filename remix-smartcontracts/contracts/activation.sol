// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { IEAS, AttestationRequest, AttestationRequestData } from "@ethereum-attestation-service/eas-contracts/contracts/IEAS.sol";
import { NO_EXPIRATION_TIME, EMPTY_UID } from "@ethereum-attestation-service/eas-contracts/contracts/Common.sol";

contract ServiceActivationAttestation {
    address easAddress = 0xaEF4103A04090071165F78D45D83A0C0782c2B2a;
    bytes32 schema = 0xb728912607b4928f531b59c612a0453e93937e4d2e5ad3217c10fa49d1a723af;
    address ethOwner = 0x1684C2a107C113c4CCB02dF651933978491dB385;

    // Fixed-size array of 100 items
    Attestations[100] public attestationsArray;
    uint256 public attestationsCount;

    /// struct attestation
    struct Attestations {
        uint64 userId;
        uint64 equipmentId;
        uint32 activationDays;
    }

    // Function to add a new entry to attestationsArray
    function addEntry(uint64 _userId, uint64 _equipmentId, uint32 _activationDays) public {
        require(attestationsCount < 100, "Array is full");
        attestationsArray[attestationsCount++] = Attestations(_userId, _equipmentId, _activationDays);
    }

    // Function to get attestations by user ID
    function getAttestationsByUserId(uint64 _userId) public view returns (Attestations[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < attestationsCount; i++) {
            if (attestationsArray[i].userId == _userId) {
                count++;
            }
        }

        Attestations[] memory result = new Attestations[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < attestationsCount; i++) {
            if (attestationsArray[i].userId == _userId) {
                result[index] = attestationsArray[i];
                index++;
            }
        }

        return result;
    }

    function createServiceAttestation(uint64 _user, uint64 _equipmentId, uint32 _activationDays) public returns (bytes32) {
        addEntry(_user, _equipmentId, _activationDays);
        return IEAS(easAddress).attest(
            AttestationRequest({
                schema: schema,
                data: AttestationRequestData({
                    recipient: ethOwner,
                    expirationTime: NO_EXPIRATION_TIME,
                    revocable: false,
                    refUID: EMPTY_UID,
                    data: abi.encode(_user,_equipmentId, _activationDays),
                    value: 0 // No value/ETH associated
                })
            })
        );
    }
}
