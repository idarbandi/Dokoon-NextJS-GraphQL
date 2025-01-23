import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './title';

// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod, amount) {
  return { id, date, name, shipTo, paymentMethod, amount };
}

const rows = [
  createData(0, '14 فروردین، 1404', 'علی رضایی', 'تهران، ایران', 'کارت ملی ***-****-****-1234', 1245000),
  createData(1, '14 فروردین، 1404', 'فاطمه حسینی', 'شیراز، ایران', 'کارت بانک ملت ****-****-****-9876', 7890000),
  createData(2, '14 فروردین، 1404', 'حسن محمدی', 'اصفهان، ایران', 'درگاه پرداخت زرین‌پال', 348500),
  createData(3, '13 فروردین، 1404', 'زهرا احمدی', 'مشهد، ایران', 'کارت اعتباری صادرات ****-****-****-5678', 2570000),
  createData(4, '12 فروردین، 1404', 'محمد حسین‌پور', 'تبریز، ایران', 'کیف پول دیجی‌کالا', 897200),
];

function preventDefault(event) {
  event.preventDefault();
}

export default function Orders() {
  return (
    <React.Fragment>
      <Title>سفارش‌های اخیر</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>تاریخ</TableCell>
            <TableCell>نام</TableCell>
            <TableCell>آدرس ارسال</TableCell>
            <TableCell>روش پرداخت</TableCell>
            <TableCell align="right">مبلغ فروش</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
              <TableCell align="right">{`${row.amount.toLocaleString('fa-IR')} ریال`}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        مشاهده‌ی سفارش‌های بیشتر
      </Link>
    </React.Fragment>
  );
}