package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net"
	"time"
)

const (
	TCP  = "tcp"
	HOST = "localhost"
	PORT = "8080"
)

var addr = HOST + ":" + PORT

type Request struct {
	Name string
}

func main() {
	server, err := net.Listen(TCP, addr)
	if err != nil {
		panic(err)
	}

	defer server.Close()

	go func() {
		for {
			conn, e := net.Dial(TCP, addr)
			if e != nil {
				panic(e)
			}
			defer conn.Close()
			conn.Write([]byte("{\"name\": \"Hung\"}"))

			time.Sleep(time.Second * 2)
		}
	}()

	for {
		conn, err := server.Accept()
		if err != nil {
			panic(err)
		}

		go handle(conn)
	}
}

func handle(conn net.Conn) {
	defer conn.Close()
	buf := make([]byte, 1024)
	len, err := conn.Read(buf)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("received ", string(buf))

	var req Request
	if err := json.Unmarshal(buf[:len], &req); err != nil {
		log.Println(err)
		return
	}

	if req.Name == "" {
		conn.Write([]byte("no name"))
		return
	}

	t := time.Now()
	conn.Write([]byte("Hi" + req.Name + "\n"))
	conn.Write([]byte(t.String()))
}
