# coding: utf-8
from sqlalchemy import BigInteger, Column, Integer, Numeric, String, Time, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
import time
Base = declarative_base()
metadata = Base.metadata



class ZerodhaStreamQuotesModelLtp(Base):
    """
         SQLAlchemy Model for the LTP Mode Stream Quotes
    """
    __tablename__ = 'zerodhastreamquotes_modeltp'
    Id = Column(Integer, primary_key=True)
    InstrumentToken = Column(String(32), primary_key=True, nullable=False)
    Tradeable = Column(Boolean, nullable=False)
    Timestamp = Column(TIMESTAMP, primary_key=True, nullable=False)
    LastTradedPrice = Column(Numeric(20, 4), nullable=False)
    Mode = Column(String(6), nullable=False)


class ZerodhaStreamQuotesModeFull(Base):
    """
     SQLAlchemy Model for the Full Mode Stream Quotes
    """
    __tablename__ = 'zerodhastreamquotes_modefull'

    Time = Column(TIMESTAMP, primary_key=True, nullable=False)
    InstrumentToken = Column(String(32), primary_key=True, nullable=False)
    LastTradedPrice = Column(Numeric(20, 4), nullable=False)
    LastTradedQty = Column(BigInteger, nullable=False)
    AvgTradedPrice = Column(Numeric(20, 4), nullable=False)
    Volume = Column(BigInteger, nullable=False)
    BuyQty = Column(BigInteger, nullable=False)
    SellQty = Column(BigInteger, nullable=False)
    OpenPrice = Column(Numeric(20, 4), nullable=False)
    HighPrice = Column(Numeric(20, 4), nullable=False)
    LowPrice = Column(Numeric(20, 4), nullable=False)
    ClosePrice = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid1Qty = Column(BigInteger, nullable=False)
    MarketDepthBid1Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid1Orders = Column(Integer, nullable=False)
    MarketDepthBid2Qty = Column(BigInteger, nullable=False)
    MarketDepthBid2Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid2Orders = Column(Integer, nullable=False)
    MarketDepthBid3Qty = Column(BigInteger, nullable=False)
    MarketDepthBid3Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid3Orders = Column(Integer, nullable=False)
    MarketDepthBid4Qty = Column(BigInteger, nullable=False)
    MarketDepthBid4Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid4Orders = Column(Integer, nullable=False)
    MarketDepthBid5Qty = Column(BigInteger, nullable=False)
    MarketDepthBid5Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthBid5Orders = Column(Integer, nullable=False)
    MarketDepthOffer1Qty = Column(BigInteger, nullable=False)
    MarketDepthOffer1Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthOffer1Orders = Column(Integer, nullable=False)
    MarketDepthOffer2Qty = Column(BigInteger, nullable=False)
    MarketDepthOffer2Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthOffer2Orders = Column(Integer, nullable=False)
    MarketDepthOffer3Qty = Column(BigInteger, nullable=False)
    MarketDepthOffer3Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthOffer3Orders = Column(Integer, nullable=False)
    MarketDepthOffer4Qty = Column(BigInteger, nullable=False)
    MarketDepthOffer4Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthOffer4Orders = Column(Integer, nullable=False)
    MarketDepthOffer5Qty = Column(BigInteger, nullable=False)
    MarketDepthOffer5Price = Column(Numeric(20, 4), nullable=False)
    MarketDepthOffer5Orders = Column(Integer, nullable=False)


def init_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata.bind = engine
    metadata.create_all(checkfirst=True)
    
    
    ltp_model = ZerodhaStreamQuotesModelLtp()
    #.insert().values(InstrumentToken='1234', Tradeable=True, Time=time.time(), LastTradedPrice=123, Mode='ltp')




