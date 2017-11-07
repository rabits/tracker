//--------------------------------------------------------------------------------------
// Created by TunerPro. Hand editing is *not* recommended or supported.
//--------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------
//--------------------------------- HEADER ------------------------------------
//--------------------------------------------------------------------------------------

{
	fDefFrmtVers             =1.21;
	strDefVersion            =1.0;
	strDefTitle              =1227148 - Turbo Buick 86-90;
	strAuthor                =Mark Mansur;
	strEngine                =3.8L LC2;
	strYear                  =1987, 88, 89, 90;
	strVINCode               =3, 7, B;
	strCodeMask              =31T;
	strComments              =TunerPro RT Datastream Definition - 10/16/03;
	iBaud                    =160;
	dwFlags                  =0x00000000;
	dwCSID                   =0x0000514C;
	btNumDumpRequests        =1;

	strCommandName           =160 Baud - No command;
	rgbtCommand              =;
	iTotalBytesInCommand     =0;
	bChecksumCommand         =0;
	iNumBytesInPayload       =25;
	iNumBytesBeforePayload   =-1;
	bMaster                  =1;
	bMonitor                 =1;
	iChainTo                 =-1;
}

//--------------------------------------------------------------------------------------
//---------------------------------- DASH -------------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =6;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =0;

	btNumGauges              =6;
	strIDsDisplayed          =3,6,8,12,5,14,;
	btNumMonitors            =4;
	strMonsDisplayed         =0,0,0,0,;
}

//--------------------------------------------------------------------------------------
//--------------------------------- VALUES ------------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =1;

	btByteNumber             =0;
	btMessageNumber          =0;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =-=General=-;
	strUnitLabel             =;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =2;

	btByteNumber             =2;
	btMessageNumber          =1;
	dwItemSizeBits           =16;
	dwOperation              =2;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =PROM ID;
	strUnitLabel             =;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =3;

	btByteNumber             =9;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.019600;
	dOffset                  =0.000000;
	strItemTitle             =Throttle Position;
	strUnitLabel             =Volts;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =4;

	btByteNumber             =4;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =IAC Present Position;
	strUnitLabel             =Steps;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =5;

	btByteNumber             =5;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =1.350000;
	dOffset                  =-40.000000;
	strItemTitle             =Coolant Temp;
	strUnitLabel             =Deg F;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =6;

	btByteNumber             =6;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Vehicle Speed;
	strUnitLabel             =MPH;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =7;

	btByteNumber             =7;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Load;
	strUnitLabel             =% DC;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =8;

	btByteNumber             =8;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =25.000000;
	dOffset                  =0.000000;
	strItemTitle             =Engine Speed;
	strUnitLabel             =RPM;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =9;

	btByteNumber             =10;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Integrator;
	strUnitLabel             =Counts;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =10;

	btByteNumber             =11;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =4.440000;
	dOffset                  =0.000000;
	strItemTitle             =O2;
	strUnitLabel             =mV;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =11;

	btByteNumber             =19;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =BLM;
	strUnitLabel             =Count;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =12;

	btByteNumber             =20;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =O2 Cross Count;
	strUnitLabel             =Crosses;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =13;

	btByteNumber             =21;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =0.352941;
	dOffset                  =0.000000;
	strItemTitle             =Spark Advance;
	strUnitLabel             =Degrees;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =14;

	btByteNumber             =22;
	btMessageNumber          =1;
	dwItemSizeBits           =16;
	dwOperation              =0;
	dFactor                  =0.390625;
	dOffset                  =0.000000;
	strItemTitle             =EGR Duty Cycle;
	strUnitLabel             =DC;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =15;

	btByteNumber             =16;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =MAF;
	strUnitLabel             =;
	dwAlarmHigh              =0;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =0;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =21;

	btByteNumber             =23;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =6;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Air Temp;
	strUnitLabel             =Units;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =20;
}

//--------------------------------------------------------------------------------------
//---------------------------------- BITS -------------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =2;
	strItemComments          =;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =16;

	btByteNumber             =0;
	btMessageNumber          =0;
	btBitNumber              =0;
	strItemTitle             =-=General=-;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =17;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =TCC ;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =Locked;
	strBitClearTitle         =Unlocked;
}

{
	dwItemType               =2;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =18;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =Water Injector;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =On;
	strBitClearTitle         =Off;
}

{
	dwItemType               =2;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =19;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =A/C;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =Requested;
	strBitClearTitle         =Not Requested;
}

{
	dwItemType               =2;
	strItemComments          =;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =0;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =Rich/Lean;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =Rich;
	strBitClearTitle         =Lean;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =22;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =Learn Control;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =Enabled;
	strBitClearTitle         =Disabled;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =23;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =Loop Status;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =Closed;
	strBitClearTitle         =Open;
}

//--------------------------------------------------------------------------------------
//---------------------------- LOOKUP TABLES ----------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =5;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =20;

	btDataType               =2;
	wTableSize               =256;
	wIndexSize               =4;
	strTableName             =Air Temp Lookup;
	dwReserved               =0;
	dwReserved               =0;
	pbtData                  =				 30, -0.40
				 35, 6.80
				 40, 14.00
				 45, 21.20
				 50, 26.60
				 55, 33.80
				 60, 41.00
				 65, 48.20
				 70, 55.40
				 75, 60.80
				 80, 68.00
				 85, 75.20
				 90, 82.40
				 95, 87.80
				 100, 95.00
				 105, 102.20
				 110, 109.40
				 115, 114.80
				 120, 122.00
				 125, 129.20
				 130, 136.40
				 135, 141.80
				 140, 149.00
				 145, 156.20
				 150, 163.40
				 155, 168.80
				 160, 176.00
				 165, 183.20
				 170, 190.40
				 175, 195.80
				 180, 203.00
				 185, 210.20
				 190, 217.40
				 195, 221.00
				 200, 230.00
				 205, 237.20
				 210, 244.40
				 215, 249.80
				 220, 257.00
				 225, 264.20
				 230, 2431.40
				 235, 276.80
				 240, 284.00
				 245, 291.20
				 250, 298.40
				 255, 303.80;
}
