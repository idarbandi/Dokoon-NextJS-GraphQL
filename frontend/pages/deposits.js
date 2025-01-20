// Deposits.js
import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Title from './title';

function preventDefault(event) {
  event.preventDefault();
}

// Function to format numbers with Persian numerals and thousands separators
function formatNumberWithPersian(number) {
  const persianDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
  const numberString = number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); // Add thousands separators
  let formattedNumber = '';

  for (let i = 0; i < numberString.length; i++) {
    const digit = numberString[i];
    if (/\d/.test(digit)) {
      formattedNumber += persianDigits[parseInt(digit)];
    } else {
      formattedNumber += digit; // Keep non-digit characters (like commas)
    }
  }
  return formattedNumber;
}

export default function Deposits() {
  const depositAmount = 3024000; // Example deposit amount in Rials
  const formattedAmount = formatNumberWithPersian(depositAmount);
  const depositDate = new Date('2024-03-15');
  const persianDate = new Intl.DateTimeFormat('fa-IR', { dateStyle: 'long' }).format(depositDate);

  return (
    <React.Fragment>
      <Title>واریزهای اخیر</Title> {/* Recent Deposits in Persian */}
      <Typography component="p" variant="h4">
        {formattedAmount} ریال {/* Display amount in Rials with Persian formatting*/}
      </Typography>
      <Typography color="text.secondary" sx={{ flex: 1 }}>
        در {persianDate} {/* Display date in Persian */}
      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          مشاهده موجودی {/* View balance in Persian */}
        </Link>
      </div>
    </React.Fragment>
  );
}
