SELECT `﻿company_ticker`,`name` FROM `stockuser`.`ticker` where name like 'Ame%';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'AMD';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'ARQL';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'AU';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'BHP';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'BLIN';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'BOSC';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'BP';
SELECT * FROM stockuser.ticker where `ticker`.`﻿company_ticker` = 'CVX';

update stockuser.stocks set company_name = 'Advanced Micro Devices, Inc.' where ticker = 'AMD';
update stockuser.stocks set company_name = 'ArQule, Inc.' where ticker = 'ARQL';
update stockuser.stocks set company_name = 'AngloGold Ashanti Limited' where ticker = 'AU';
update stockuser.stocks set company_name = 'BHP Billiton Limited' where ticker = 'BHP';
update stockuser.stocks set company_name = 'Bridgeline Digital, Inc.' where ticker = 'BLIN';
update stockuser.stocks set company_name = 'B.O.S. Better Online Solutions Ltd.' where ticker = 'BOSC';
update stockuser.stocks set company_name = 'BP p.l.c.' where ticker = 'BP';
update stockuser.stocks set company_name = 'Chevron Corporation' where ticker = 'CVX';

select company_name,ticker,calendardate,pe,pb,fcf,stock_return
  from stockuser.stocks
 where stock_return != '';
