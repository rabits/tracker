//--------------------------------------------------------------------------------------
// Created by TunerPro. Hand editing is *not* recommended or supported.
//--------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------
//--------------------------------- HEADER ------------------------------------
//--------------------------------------------------------------------------------------

{
	fDefFrmtVers             =1.21;
	strDefVersion            =Version 1.0;
	strDefTitle              =A008;
	strAuthor                =Robert Saar;
	strEngine                =3.8;
	strYear                  =86-89;
	strVINCode               =3, B, 7;
	strCodeMask              =?;
	strComments              =check A008.ADS for specific details. use a 10K(if desired, datastream changes). robertisaar@yahoo.com for comments/questions.;
	iBaud                    =160;
	dwFlags                  =0x00000000;
	dwCSID                   =0x00016FD9;
	btNumDumpRequests        =1;

	strCommandName           =160 Baud;
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
	strIDsDisplayed          =0,0,0,0,0,0,;
	btNumMonitors            =4;
	strMonsDisplayed         =0,0,0,0,;
}

//--------------------------------------------------------------------------------------
//--------------------------------- VALUES ------------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =9;

	btByteNumber             =2;
	btMessageNumber          =1;
	dwItemSizeBits           =16;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =PROM ID;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =10;

	btByteNumber             =4;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =IAC Position;
	strUnitLabel             =Steps;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =11;

	btByteNumber             =5;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =6;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Coolant Temp C;
	strUnitLabel             =*C;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =12;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =14;

	btByteNumber             =5;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =6;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Coolant Temp F;
	strUnitLabel             =F;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =13;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =15;

	btByteNumber             =6;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Vehicle Speed;
	strUnitLabel             =MPH;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =16;

	btByteNumber             =7;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =LV8;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =17;

	btByteNumber             =8;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =25.000000;
	dOffset                  =0.000000;
	strItemTitle             =Engine Speed;
	strUnitLabel             =RPM;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =18;

	btByteNumber             =9;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.019600;
	dOffset                  =0.000000;
	strItemTitle             =TPS;
	strUnitLabel             =Volts;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =19;

	btByteNumber             =10;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =INT;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =20;

	btByteNumber             =11;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =4.440000;
	dOffset                  =0.000000;
	strItemTitle             =O2 Sensor;
	strUnitLabel             =mV;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =21;

	btByteNumber             =18;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Knock Counter;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =22;

	btByteNumber             =19;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =BLM;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =23;

	btByteNumber             =20;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Rich/Lean Transition Counter;
	strUnitLabel             =Transitions;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =60;

	btByteNumber             =16;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =MAF;
	strUnitLabel             =Grams/Sec;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =56;

	btByteNumber             =21;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.352941;
	dOffset                  =0.000000;
	strItemTitle             =Spark Advance;
	strUnitLabel             =*;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =66;

	btByteNumber             =22;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.392157;
	dOffset                  =0.000000;
	strItemTitle             =EGR Duty Cycle;
	strUnitLabel             =%;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =conversion may be bad, document isn't very clear on it.;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =71;

	btByteNumber             =23;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =6;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Air Temp Sensor C;
	strUnitLabel             =C;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =67;
}

{
	dwItemType               =1;
	strItemComments          =conversion may be bad, document isn't very clear on it.;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =72;

	btByteNumber             =23;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =6;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Air Temp Sensor F;
	strUnitLabel             =F;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =70;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =73;

	btByteNumber             =0;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =ALDL Pin A-B Open Values;
	strUnitLabel             =Units;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =76;

	btByteNumber             =21;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.176471;
	dOffset                  =0.000000;
	strItemTitle             =Knock Retard;
	strUnitLabel             =*;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =77;

	btByteNumber             =23;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =0;
	dFactor                  =0.100000;
	dOffset                  =0.000000;
	strItemTitle             =Battery Voltage;
	strUnitLabel             =Volts;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

{
	dwItemType               =1;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =78;

	btByteNumber             =24;
	btMessageNumber          =1;
	dwItemSizeBits           =8;
	dwOperation              =3;
	dFactor                  =1.000000;
	dOffset                  =0.000000;
	strItemTitle             =Counter since No Malfunctions;
	strUnitLabel             =;
	dwAlarmHigh              =255;
	bAlarmHighENable         =0;
	dwAlarmLow               =0;
	bAlarmLowEnable          =0;
	iRangeHigh               =255;
	iRangeLow                =0;
	iLookupTableIndex        =-1;
}

//--------------------------------------------------------------------------------------
//---------------------------------- BITS -------------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =1;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Mode Byte 2;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =2;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Road Speed Pulse;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =OCCURRED;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =3;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =ESC Failure;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =4;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =Reference Pulse;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =5;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =Diagnostic Switch in 3.9K(Factory Test) Mode;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =6;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =Diagnostic Switch in Shorted(Field Test) Mode;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =7;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =Diagnostic Switch in 10K(ALDL) Mode;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =8;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =Battery Voltage High;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =74;

	btByteNumber             =1;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =Air Meter Pulse Occurred;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =24;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Malfunction Byte 1;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =25;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =12 - No Reference Pulses;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =26;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =13 - O2 Sensor Open;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =27;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =14 - Coolant Temp High;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =28;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =15 - Coolant Temp Low;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =29;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =21 - TPS High;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =30;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =22 - TPS Low;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =32;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =23 - Air Temp Sensor Low;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =31;

	btByteNumber             =12;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =24 - VSS;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =34;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Malfunction Byte 2;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =33;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =25 - Air Temp Sensor High;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =35;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =31 - Wastegate;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =36;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =32 - EGR;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =37;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =33 - MAF High;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =38;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =34 - MAF Low;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =39;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =35 - IAC;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =40;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =41 - Cam Sensor;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =41;

	btByteNumber             =13;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =42 - EST Monitor;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =42;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Malfunction Byte 3;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =43;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =43 - ESC;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =44;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =44 - O2 Lean;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =45;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =45 - O2 Rich;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =46;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =51 - PROM;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =47;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =52 - CAL-PACK;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =48;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =53 - N/A;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =49;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =54 - N/A;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =50;

	btByteNumber             =14;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =55 - A/D Unit;
	bAlarmSetEnable          =1;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ERROR;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =51;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Air/Fuel Mode Byte;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =52;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =Cranked In Clear Flood;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =53;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =BLM Enable;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =55;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =Prop Step;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =RICH;
	strBitClearTitle         =LEAN;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =57;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =First Time Closed Loop;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =58;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =Rich/Lean;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =RICH;
	strBitClearTitle         =LEAN;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =59;

	btByteNumber             =15;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =Loop Status;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =1;
	strBitSetTitle           =CLOSED;
	strBitClearTitle         =OPEN;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =1;
	bVisible                 =1;
	dwUniqueID               =61;

	btByteNumber             =0;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =I/O Byte 1;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =1;
	strBitClearTitle         =0;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =62;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =0;
	strItemTitle             =P/N Position Switch;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =PARK/NEUTRAL;
	strBitClearTitle         =DRIVE;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =63;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =1;
	strItemTitle             =Cruise Control;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ENGAGED;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =64;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =2;
	strItemTitle             =TCC;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =LOCKED;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =65;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =3;
	strItemTitle             =Power Steering Switch;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =YES;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =75;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =4;
	strItemTitle             =Water Injector;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =ON;
	strBitClearTitle         =;
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =54;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =5;
	strItemTitle             =3rd Gear Switch;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =OPEN;
	strBitClearTitle         =CLOSED(YES);
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =68;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =6;
	strItemTitle             =4th Gear Switch;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =OPEN;
	strBitClearTitle         =CLOSED(YES);
}

{
	dwItemType               =2;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =69;

	btByteNumber             =17;
	btMessageNumber          =1;
	btBitNumber              =7;
	strItemTitle             =A/C Request;
	bAlarmSetEnable          =0;
	bAlarmNotSetEnable       =0;
	strBitSetTitle           =;
	strBitClearTitle         =REQUESTED;
}

//--------------------------------------------------------------------------------------
//---------------------------- LOOKUP TABLES ----------------------------------
//--------------------------------------------------------------------------------------

{
	dwItemType               =5;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =12;

	btDataType               =2;
	wTableSize               =256;
	wIndexSize               =4;
	strTableName             =Coolant Temp C;
	dwReserved               =0;
	dwReserved               =0;
	pbtData                  =				 30, -18.00
				 35, -14.00
				 40, -10.00
				 45, -6.00
				 50, -3.00
				 55, 1.00
				 60, 5.00
				 65, 9.00
				 70, 13.00
				 75, 16.00
				 80, 20.00
				 85, 24.00
				 90, 28.00
				 95, 31.00
				 100, 35.00
				 105, 39.00
				 110, 43.00
				 115, 46.00
				 120, 50.00
				 125, 54.00
				 130, 58.00
				 135, 61.00
				 140, 65.00
				 145, 69.00
				 150, 73.00
				 155, 76.00
				 160, 80.00
				 165, 84.00
				 170, 88.00
				 175, 91.00
				 180, 95.00
				 185, 99.00
				 190, 103.00
				 195, 105.00
				 200, 110.00
				 205, 114.00
				 210, 118.00
				 215, 121.00
				 220, 125.00
				 225, 129.00
				 230, 133.00
				 235, 136.00
				 240, 140.00
				 245, 144.00
				 250, 148.00
				 255, 151.00;
}

{
	dwItemType               =5;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =13;

	btDataType               =2;
	wTableSize               =256;
	wIndexSize               =4;
	strTableName             =Coolant Temp F;
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
				 230, 271.40
				 235, 276.80
				 240, 284.00
				 245, 291.20
				 250, 298.40
				 255, 303.80;
}

{
	dwItemType               =5;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =67;

	btDataType               =2;
	wTableSize               =256;
	wIndexSize               =4;
	strTableName             =Air Temp Sensor C ;
	dwReserved               =0;
	dwReserved               =0;
	pbtData                  =0, -40.00
				 15, -25.00
				 31, -12.00
				 47, -3.00
				 63, 4.00
				 79, 11.00
				 95, 16.00
				 111, 22.00
				 127, 27.00
				 143, 33.00
				 159, 39.00
				 175, 46.00
				 191, 54.00
				 207, 64.00
				 223, 77.00
				 239, 102.00
				 255, 151.00;
}

{
	dwItemType               =5;
	strItemComments          =<Comments>;
	bSeparator               =0;
	bVisible                 =1;
	dwUniqueID               =70;

	btDataType               =2;
	wTableSize               =256;
	wIndexSize               =4;
	strTableName             =Air Temp Sensor F;
	dwReserved               =0;
	dwReserved               =0;
	pbtData                  =0, -40.00
				 15, -13.00
				 31, 10.40
				 47, 26.60
				 63, 39.20
				 79, 51.80
				 95, 60.80
				 111, 71.60
				 127, 80.60
				 143, 91.40
				 159, 102.20
				 175, 114.80
				 191, 129.20
				 207, 147.20
				 223, 170.60
				 239, 215.60
				 255, 303.80;
}
