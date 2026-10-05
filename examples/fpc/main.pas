program employee_top5;

{$mode objfpc}{$H+}

uses
  SysUtils, SQLDB, IBConnection;

var
  Con: TIBConnection;
  Tr: TSQLTransaction;
  Q: TSQLQuery;

begin
  Con := TIBConnection.Create(nil);
  Tr := TSQLTransaction.Create(nil);
  Q := TSQLQuery.Create(nil);
  try
    Con.DatabaseName := 'firebird:/var/lib/firebird/data/employee.fdb';
    Con.UserName := 'SYSDBA';
    Con.Password := 'masterkey';
    Con.Transaction := Tr;
    Q.Database := Con;
    Q.Transaction := Tr;
    Q.SQL.Text :=
      'SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ' +
      'ORDER BY SALARY DESC ROWS 5';
    Con.Open;
    Q.Open;
    WriteLn('Топ-5 сотрудников по зарплате:');
    while not Q.EOF do
    begin
      WriteLn(Format('  %s %s — %.2f',
        [Q.FieldByName('FIRST_NAME').AsString,
         Q.FieldByName('LAST_NAME').AsString,
         Q.FieldByName('SALARY').AsFloat]));
      Q.Next;
    end;
    Con.Close;
  finally
    Q.Free;
    Tr.Free;
    Con.Free;
  end;
end.
