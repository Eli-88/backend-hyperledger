/*
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"chaincode-go/chaincode"
	"log"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

func main() {
	accountChaincode, err := contractapi.NewChaincode(&chaincode.SmartContract{})
	if err != nil {
		log.Panicf("Error creating balance chaincode: %v", err)
	}

	if err := accountChaincode.Start(); err != nil {
		log.Panicf("Error starting balance chaincode: %v", err)
	}
}
