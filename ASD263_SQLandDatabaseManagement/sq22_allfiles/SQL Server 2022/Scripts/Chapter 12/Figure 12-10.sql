USE [New_AP]
GO

/****** Object:  Table [dbo].[Invoices]    Script Date: 2/12/2020 4:00:29 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Invoices](
	[InvoiceID] [int] IDENTITY(1,1) NOT NULL,
	[VendorID] [int] NOT NULL,
	[InvoiceDate] [date] NULL,
	[InvoiceTotal] [money] NULL,
 CONSTRAINT [PK_Invoices_1] PRIMARY KEY CLUSTERED 
(
	[InvoiceID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[Invoices] ADD  DEFAULT ((0)) FOR [InvoiceTotal]
GO

ALTER TABLE [dbo].[Invoices]  WITH CHECK ADD  CONSTRAINT [FK_Invoices_Vendors] FOREIGN KEY([VendorID])
REFERENCES [dbo].[Vendors] ([VendorID])
GO

ALTER TABLE [dbo].[Invoices] CHECK CONSTRAINT [FK_Invoices_Vendors]
GO

ALTER TABLE [dbo].[Invoices]  WITH CHECK ADD  CONSTRAINT [CK_InvoiceTotal] CHECK  (([InvoiceTotal]>(0)))
GO

ALTER TABLE [dbo].[Invoices] CHECK CONSTRAINT [CK_InvoiceTotal]
GO


