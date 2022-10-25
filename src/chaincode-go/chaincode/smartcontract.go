package chaincode

import (
	"encoding/json"
	"fmt"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract provides functions for managing an Asset
type SmartContract struct {
	contractapi.Contract
}

type Account struct {
	Amount    float64 `json:"Amount"`
	ID        string  `json:"ID"`
	PublicKey string  `json:"PublicKey"`
}

func (s *SmartContract) InitBalance(ctx contractapi.TransactionContextInterface, id string, amount float64, publicKey string) error {
	balanceJson, err := ctx.GetStub().GetState(id)

	// if the balance already exists, just return
	if balanceJson != nil {
		return fmt.Errorf("%s already exists", id)
	}

	if err != nil {
		return err
	}

	balance := Account{
		ID:        id,
		Amount:    amount,
		PublicKey: publicKey,
	}

	balanceJson, err = json.Marshal(balance)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(id, balanceJson)
}

func (s *SmartContract) GetAccount(ctx contractapi.TransactionContextInterface, id string) (*Account, error) {
	balanceJson, err := ctx.GetStub().GetState(id)
	if err != nil {
		return nil, err
	}

	if balanceJson == nil {
		return nil, fmt.Errorf("%s does not exists", id)
	}

	balance := &Account{}
	err = json.Unmarshal(balanceJson, balance)
	return balance, err
}

func (s *SmartContract) GetBalance(ctx contractapi.TransactionContextInterface, id string) (float64, error) {
	balanceJson, err := ctx.GetStub().GetState(id)
	if err != nil {
		return float64(0), err
	}

	if balanceJson == nil {
		return float64(0), fmt.Errorf("%s does not exists", id)
	}

	account := Account{}
	err = json.Unmarshal(balanceJson, &account)
	return account.Amount, err
}

func (s *SmartContract) Send(ctx contractapi.TransactionContextInterface, fromId string, toId string, amount float64) error {
	fromBalance, err := s.GetAccount(ctx, fromId)
	if err != nil {
		return err
	}

	if fromBalance.Amount < amount {
		return fmt.Errorf("the balance in id %s is too low for transfer", fromId)
	}

	toBalance, err := s.GetAccount(ctx, toId)
	if err != nil {
		return err
	}
	toBalance.Amount = toBalance.Amount + amount

	toBalanceJson, err := json.Marshal(toBalance)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(toId, toBalanceJson)
}
