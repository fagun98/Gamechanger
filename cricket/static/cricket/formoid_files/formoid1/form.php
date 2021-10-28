<?php

define('EMAIL_FOR_REPORTS', '');
define('RECAPTCHA_PRIVATE_KEY', '@privatekey@');
define('FINISH_URI', 'http://');
define('FINISH_ACTION', 'redirect');
define('FINISH_MESSAGE', 'Thanks for filling out my form!');
define('UPLOAD_ALLOWED_FILE_TYPES', 'doc, docx, xls, csv, txt, rtf, html, zip, jpg, jpeg, png, gif');

define('_DIR_', str_replace('\\', '/', dirname(__FILE__)) . '/');
require_once _DIR_ . '/handler.php';

?>

<?php if (frmd_message()): ?>
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-biz-green.css" type="text/css" />
<span class="alert alert-success"><?php echo FINISH_MESSAGE; ?></span>
<?php else: ?>
<!-- Start Formoid form-->
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-biz-green.css" type="text/css" />
<script type="text/javascript" src="<?php echo dirname($form_path); ?>/jquery.min.js"></script>
<form class="formoid-biz-green" style="background-color:#1A2223;font-size:14px;font-family:'Open Sans','Helvetica Neue', 'Helvetica', Arial, Verdana, sans-serif;color:#ECECEC;max-width:480px;min-width:150px" method="post"><div class="title"><h2>Formation</h2></div>
	<div class="element-select<?php frmd_add_class("select"); ?>" title="Type of match "><label class="title"><span class="required">*</span></label><div class="large"><span><select name="select" required="required">

		<option value="T20">T20</option>
		<option value="Test">Test</option>
		<option value="ODI">ODI</option></select><i></i></span></div></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Batsmen</h3></div>
	<div class="element-select<?php frmd_add_class("select1"); ?>" title="Number of batsmen "><label class="title"><span class="required">*</span></label><div class="large"><span><select name="select1" required="required">

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-radio<?php frmd_add_class("radio"); ?>" title="Specify Batsmen"><label class="title">Specify Batsmen</label>		<div class="column column1"><label><input type="radio" name="radio" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-select<?php frmd_add_class("select3"); ?>" title="Right-handed Batsmen"><label class="title"></label><div class="large"><span><select name="select3" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-select<?php frmd_add_class("select2"); ?>" title="Left-handed Batsmen"><label class="title"></label><div class="large"><span><select name="select2" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Bowlers</h3></div>
	<div class="element-select<?php frmd_add_class("select4"); ?>" title="Number of bowlers "><label class="title"><span class="required">*</span></label><div class="large"><span><select name="select4" required="required">

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-select<?php frmd_add_class("select5"); ?>" title="Number of pacers "><label class="title"></label><div class="large"><span><select name="select5" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-radio<?php frmd_add_class("radio1"); ?>" title="Specify Pacers
"><label class="title">Specify Pacers
</label>		<div class="column column1"><label><input type="radio" name="radio1" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio1" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-select<?php frmd_add_class("select6"); ?>" title="Right-handed Pacers "><label class="title"></label><div class="large"><span><select name="select6" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-select<?php frmd_add_class("select7"); ?>" title="Left-handed Pacers "><label class="title"></label><div class="large"><span><select name="select7" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-select<?php frmd_add_class("select8"); ?>" title="Number of spinners "><label class="title"></label><div class="large"><span><select name="select8" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-radio<?php frmd_add_class("radio2"); ?>" title="Specify Spinners
"><label class="title">Specify Spinners
</label>		<div class="column column1"><label><input type="radio" name="radio2" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio2" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-select<?php frmd_add_class("select9"); ?>" title="Right-handed Spinners "><label class="title"></label><div class="large"><span><select name="select9" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-select<?php frmd_add_class("select10"); ?>" title="Left-handed Spinners "><label class="title"></label><div class="large"><span><select name="select10" >

		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option></select><i></i></span></div></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Weeket-keepers</h3></div>
	<div class="element-select<?php frmd_add_class("select11"); ?>" title="Number of wicket-keepers "><label class="title"></label><div class="large"><span><select name="select11" >

		<option value="1">1</option>
		<option value="2">2</option></select><i></i></span></div></div>
<div class="submit"><input type="submit" value="Submit"/></div></form><script type="text/javascript" src="<?php echo dirname($form_path); ?>/formoid-biz-green.js"></script>

<!-- Stop Formoid form-->
<?php endif; ?>

<?php frmd_end_form(); ?>