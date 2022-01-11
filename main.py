# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

from suhu_laut import suhu
import numpy

from PIL import Image

###########################################################################
## Class MainDialogBase
###########################################################################

class MainDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Perubahan Suhu Permukaan Laut Selat Bali Tahun 2020 dengan Tahun 2021"), pos = wx.DefaultPosition, size = wx.Size( 1361,752 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		mainSizer = wx.BoxSizer( wx.HORIZONTAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Input Citra Tahun 2020") ), wx.VERTICAL )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText64 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, _(u"Input Band 10"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		bSizer44.Add( self.m_staticText64, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 225,225 ), 0 )
		self.m_bitmap1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer44.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		self.m_filePicker34 = wx.FilePickerCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer44.Add( self.m_filePicker34, 0, wx.ALL, 5 )


		sbSizer21.Add( bSizer44, 0, wx.EXPAND, 5 )


		bSizer21.Add( sbSizer21, 1, wx.EXPAND, 5 )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u" Input Citra Tahun 2021") ), wx.VERTICAL )

		bSizer421 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText621 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, _(u"Input Band 10"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText621.Wrap( -1 )

		bSizer421.Add( self.m_staticText621, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 225,225 ), 0 )
		self.m_bitmap2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer421.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		self.m_filePicker321 = wx.FilePickerCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer421.Add( self.m_filePicker321, 0, wx.ALL, 5 )


		sbSizer31.Add( bSizer421, 0, wx.EXPAND, 5 )


		bSizer21.Add( sbSizer31, 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Clip dengan Polygon (2020)") ), wx.VERTICAL )

		bSizer441 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText641 = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, _(u"Input Polygon"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText641.Wrap( -1 )

		bSizer441.Add( self.m_staticText641, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_filePicker341 = wx.FilePickerCtrl( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer441.Add( self.m_filePicker341, 0, wx.ALL, 5 )

		self.m_bitmap11 = wx.StaticBitmap( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 225,225 ), 0 )
		self.m_bitmap11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer441.Add( self.m_bitmap11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sbSizer211.Add( bSizer441, 0, wx.EXPAND, 5 )


		bSizer211.Add( sbSizer211, 1, wx.EXPAND, 5 )

		sbSizer311 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Clip dengan Polygon (2021)") ), wx.VERTICAL )

		bSizer4211 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6211 = wx.StaticText( sbSizer311.GetStaticBox(), wx.ID_ANY, _(u"Input Polygon"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6211.Wrap( -1 )

		bSizer4211.Add( self.m_staticText6211, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_filePicker3211 = wx.FilePickerCtrl( sbSizer311.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer4211.Add( self.m_filePicker3211, 0, wx.ALL, 5 )

		self.m_bitmap21 = wx.StaticBitmap( sbSizer311.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 225,225 ), 0 )
		self.m_bitmap21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer4211.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sbSizer311.Add( bSizer4211, 0, wx.EXPAND, 5 )


		bSizer211.Add( sbSizer311, 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer211, 1, wx.EXPAND, 5 )

		bSizer3211 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer1121 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Pemrosesan SPL Tahun 2020") ), wx.VERTICAL )

		sbSizer1121.SetMinSize( wx.Size( 200,200 ) )
		self.m_staticText531 = wx.StaticText( sbSizer1121.GetStaticBox(), wx.ID_ANY, _(u"TOA Radiance"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )

		sbSizer1121.Add( self.m_staticText531, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button1331 = wx.Button( sbSizer1121.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1121.Add( self.m_button1331, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bitmap3 = wx.StaticBitmap( sbSizer1121.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		self.m_bitmap3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer1121.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticline121 = wx.StaticLine( sbSizer1121.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1121.Add( self.m_staticline121, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText5121 = wx.StaticText( sbSizer1121.GetStaticBox(), wx.ID_ANY, _(u"Brightness Temperature"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5121.Wrap( -1 )

		sbSizer1121.Add( self.m_staticText5121, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button13121 = wx.Button( sbSizer1121.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1121.Add( self.m_button13121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_bitmap31 = wx.StaticBitmap( sbSizer1121.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		self.m_bitmap31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer1121.Add( self.m_bitmap31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer3211.Add( sbSizer1121, 1, wx.EXPAND, 5 )

		sbSizer11111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Pemrosesan SPL Tahun 2021") ), wx.VERTICAL )

		self.m_staticText5311 = wx.StaticText( sbSizer11111.GetStaticBox(), wx.ID_ANY, _(u"TOA Radiance"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5311.Wrap( -1 )

		sbSizer11111.Add( self.m_staticText5311, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button13311 = wx.Button( sbSizer11111.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11111.Add( self.m_button13311, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap32 = wx.StaticBitmap( sbSizer11111.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		self.m_bitmap32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer11111.Add( self.m_bitmap32, 0, wx.ALL, 5 )

		self.m_staticline1212 = wx.StaticLine( sbSizer11111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer11111.Add( self.m_staticline1212, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText51212 = wx.StaticText( sbSizer11111.GetStaticBox(), wx.ID_ANY, _(u"Brightness Temperature"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51212.Wrap( -1 )

		sbSizer11111.Add( self.m_staticText51212, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button131212 = wx.Button( sbSizer11111.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11111.Add( self.m_button131212, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap33 = wx.StaticBitmap( sbSizer11111.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		self.m_bitmap33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer11111.Add( self.m_bitmap33, 0, wx.ALL, 5 )


		bSizer3211.Add( sbSizer11111, 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer3211, 1, wx.EXPAND, 5 )

		bSizer32111 = wx.BoxSizer( wx.VERTICAL )

		sbSizer11211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Suhu Permukaan Laut Tahun 2020") ), wx.VERTICAL )

		sbSizer11211.SetMinSize( wx.Size( 200,200 ) )
		self.m_button1312121 = wx.Button( sbSizer11211.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11211.Add( self.m_button1312121, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap34 = wx.StaticBitmap( sbSizer11211.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		self.m_bitmap34.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer11211.Add( self.m_bitmap34, 0, wx.ALL, 5 )


		bSizer32111.Add( sbSizer11211, 0, wx.EXPAND, 5 )

		sbSizer112111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Suhu Permukaan Laut Tahun 2021") ), wx.VERTICAL )

		sbSizer112111.SetMinSize( wx.Size( 200,200 ) )
		self.m_button13121211 = wx.Button( sbSizer112111.GetStaticBox(), wx.ID_ANY, _(u"Mulai"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer112111.Add( self.m_button13121211, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_bitmap341 = wx.StaticBitmap( sbSizer112111.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		self.m_bitmap341.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sbSizer112111.Add( self.m_bitmap341, 0, wx.ALL, 5 )


		bSizer32111.Add( sbSizer112111, 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer32111, 1, wx.EXPAND, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		# self.Bind( wx.EVT_CLOSE, self.OnCloseDialog )
		self.m_filePicker34.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker1OnFileChanged )
		self.m_filePicker321.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker2OnFileChanged )
		self.m_filePicker341.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker3OnFileChanged )
		self.m_filePicker3211.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker4OnFileChanged )
		self.m_button1331.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button13121.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button13311.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
		self.m_button131212.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
		self.m_button1312121.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
		self.m_button13121211.Bind(wx.EVT_BUTTON, self.m_button7OnButtonClick)

	def __del__( self ):
		pass

	suhuObject = suhu()

	# Virtual event handlers, override them in your derived class
	def OnCloseDialog( self, event ):
		event.Skip()
		
	def m_filePicker1OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.suhuObject.openImage_b10_2020(path)
		if isImage:
			bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(225, 225, wx.IMAGE_QUALITY_HIGH)
			bitmapImage = wx.BitmapFromImage(image)
			self.m_bitmap1.SetBitmap(bitmapImage)
		event.Skip()
	
	def m_filePicker2OnFileChanged( self, event ):
		path = event.GetPath()
		isImage = self.suhuObject.openImage_b10_2021(path)
		if isImage:
			bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
			image = wx.ImageFromBitmap(bitmap)
			image = image.Scale(225, 225, wx.IMAGE_QUALITY_HIGH)
			bitmapImage = wx.BitmapFromImage(image)
			self.m_bitmap2.SetBitmap(bitmapImage)

		event.Skip()
	
	def m_filePicker3OnFileChanged( self, event ):
		path = event.GetPath()
		gambar = self.suhuObject.clip_b10_2020(path)
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 225, 225, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap11.SetBitmap(bitmapImage)
		event.Skip()

	def m_filePicker4OnFileChanged( self, event ):
		path = event.GetPath()
		gambar = self.suhuObject.clip_b10_2021(path)
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 225, 225, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap21.SetBitmap(bitmapImage)
		event.Skip()
	
	def m_button1OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_TOA_2020()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 250, 250, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap3.SetBitmap(bitmapImage)
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_BT_2020()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 250, 250, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap31.SetBitmap(bitmapImage)
		event.Skip()

	def m_button4OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_TOA_2021()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 250, 250, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap32.SetBitmap(bitmapImage)
		event.Skip()

	def m_button5OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_BT_2021()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 250, 250, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap33.SetBitmap(bitmapImage)
		event.Skip()

	def m_button6OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_SST_2020()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 300, 300, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap34.SetBitmap(bitmapImage)
		event.Skip()

	def m_button7OnButtonClick( self, event ):
		gambar = self.suhuObject.mulai_SST_2021()
		arrayimg = numpy.array(gambar)
		img = self.convertToImage(arrayimg, 300, 300, False)
		bitmapImage = wx.Bitmap(img)
		self.m_bitmap341.SetBitmap(bitmapImage)
		event.Skip()

	def convertToImage(self, array, w_in, h_in, isFloat):
		newW = w_in
		newH = h_in
		# print(self.segmen.TAG, "Declaring RGB")

		if isFloat:
			rgb = array * 32
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(rgb).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
			
		else:
			# print(self.segmen.TAG, "Convert Image to RGB")
			pilImage = Image.fromarray(array).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
		
		# print(self.segmen.TAG, "Resize Image")
		H = image.GetHeight()
		W = image.GetWidth()
		if (W > H):
			newH = newH * H / W
		else:
			newW = newW * W / H
		image = image.Scale(newW, newH)
		return image

class MainApp(wx.App):
 def OnInit(self):
  mainFrame = MainDialogBase(None)
  mainFrame.Show(True)
  return True

if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()

