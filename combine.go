package main

import (
  "fmt"
  "io"
  "os"
  "strings"
  "bufio"
)
type People struct{
  emails map[string] string
}

func main(){
  ps := new(People)

  ps.emails = make(map[string] string)

  var filepath_a, filepath_b, filepath_c="a","b","c"
  file_a,err := os.Open(filepath_a)
  file_b,err := os.Open(filepath_b)
  file_c,err := os.Open(filepath_c)
  // file_c,err := os.Create(output)
  if err != nil{
    panic(err)
  }
  defer file_a.Close()
  defer file_b.Close()
  defer file_c.Close()
  // defer output.Close()
  r := bufio.NewReaderSize(file_a,4*1024)
  line, isPrefix, err := r.ReadLine()
  for err == nil && !isPrefix {
    s := string(line)
    ss := strings.Fields(s)
    // fmt.Println(ss[1],ss[2])
    ps.emails[ss[2]] =ss[1]
    line, isPrefix, err = r.ReadLine()
  }
  // fmt.Println(ps.emails)
  if isPrefix {
    fmt.Println("buffer size to small")
    return
  }
  if err != io.EOF {
    fmt.Println(err)
    return
  }

  r = bufio.NewReaderSize(file_b,4*1024)
  line, isPrefix, err = r.ReadLine()
  for err == nil && !isPrefix {
    s := string(line)

    ss := strings.Fields(s)
    // fmt.Println(ss,ss[5])
    account, ok := ps.emails[ss[5]]
    if ok{
      ss = append(ss,account)
      fmt.Println(ss)
    }
    // fmt.Println(ss[1],ss[2])
    ps.emails[ss[2]] =ss[1]
    line, isPrefix, err = r.ReadLine()
  }

  r = bufio.NewReaderSize(file_c,4*1024)
  line, isPrefix, err = r.ReadLine()
  for err == nil && !isPrefix {
    s := string(line)

    ss := strings.Fields(s)
    // fmt.Println(ss,ss[5])
    account, ok := ps.emails[ss[5]]
    if ok{
      ss = append(ss,account)
      fmt.Println(ss)
    }
    // fmt.Println(ss[1],ss[2])
    ps.emails[ss[2]] =ss[1]
    line, isPrefix, err = r.ReadLine()
  }
}
